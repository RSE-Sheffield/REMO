""" Defines the client-side REMO API object """

import os
import random
import carla

import remo.carla_helpers.server
from remo.remo_metadata import RemoMetadata, RemoMetadataWriter, RemoEncounterData, RemoMetadataReader
from remo.remo_scenario_config import RemoScenarioConfiguration
import subprocess
import time

class RemoAPI:
    """ User interface for interacting with REMO """

    def __init__(self):
        """ Initialise the API object """
        self.is_day = False
        self.is_foggy = False
        self.is_wet = False
        self.active_hero_id = None
        self.metadata = RemoMetadata()
        self.poll_frequency = 1.0
        self.poll_step = 0
        self.scenario_runner_root = os.environ.get("REMO_SCENARIO_RUNNER_ROOT")
        
    # Connects to the carla server
    def connect_to_server(self):
        self.client = remo.carla_helpers.server.connect_to_carla_server()
        self.world = self.client.get_world()
        
    def configure_server(self, dt=0.05, traffic_manager_port=8000, rng_seed=57):
        print("Setting deterministic mode")
        deterministic_settings = self.world.get_settings()
        deterministic_settings.synchronous_mode = True
        deterministic_settings.fixed_delta_seconds = dt
        self.world.apply_settings(deterministic_settings)
        self.client.reload_world(False)
        
        traffic_manager = self.client.get_trafficmanager(traffic_manager_port)
        traffic_manager.set_synchronous_mode(True)
        traffic_manager.set_random_device_seed(rng_seed) # define TM seed for determinism

    # Interfaces with the carla server to prepare the correct environment and load the ads
    def load_scenario(self, scenario_config):
        print("Loading scenario " + str(scenario_config.scenario_file))
        self.metadata.scenario_file = scenario_config.scenario_file
        subprocess.Popen(["python3", "scenario_runner.py", "--scenario", self.metadata.scenario_file, "--reloadWorld"], cwd=self.scenario_runner_root)
        
        if scenario_config.ads == "manual":
            time.sleep(3.0)
            self.load_manual_control()

    def load_manual_control(self):
        print("Starting manual control")
        subprocess.Popen(["python3", self.scenario_runner_root + "/manual_control.py"], cwd=self.scenario_runner_root)
        
    # Runs the active scenario and starts recording if a recording configuration is supplied
    def run_active_scenario(self, recording_config=None):
        print("Starting scenario")
        # If we have a recording config, start recording according to it
        runtime = 20.0
        if recording_config is not None:
            print("Starting recording")
            self.metadata.replay_file = recording_config.replay_file
            self.client.start_recorder(self.metadata.replay_file)
            runtime = recording_config.recording_time
        
        # Run the scenario until end conditions are met
        start_time = time.time()
        last_time = start_time
        total_elapsed_time = 0.0
        time_since_last_poll = 0.0
        poll_period = 1.0 / self.poll_frequency
        
        while(total_elapsed_time < runtime):
            time_now = time.time()
            dt = time_now - last_time
            
            time_since_last_poll += dt
            if (time_since_last_poll > poll_period):
                self.on_poll_tick()
                time_since_last_poll -= poll_period
                self.poll_step += 1

            total_elapsed_time += dt
            last_time = time_now

        # Stop recording if we started it
        if recording_config is not None:
            print("Stopping recording")
            self.client.stop_recorder()
        
            # If we are recording, write the metadata file
            print("Writing metadata")
            metadata_writer = RemoMetadataWriter(self.metadata, recording_config.metadata_filepath)
            metadata_writer.write()

    def on_poll_tick(self):
        hero_location = self.get_hero_location()
        actors, env_objects = self.get_objects_within_radius(self.get_hero_location(), 10.0)
        for obj in env_objects:
            encounter = RemoEncounterData()            
            encounter.name = obj.name
            encounter.entity_id = obj.id
            encounter.entity_type = str(obj.type)
            encounter.distance_to_entity = hero_location.distance(obj.transform.location)
            if not self.poll_step in self.metadata.encounters:
                self.metadata.encounters[self.poll_step] = []
            self.metadata.encounters[self.poll_step].append(encounter)
        for obj in actors:
            encounter = RemoEncounterData()            
            encounter.entity_id = obj.id
            encounter.entity_type = obj.type_id
            encounter.distance_to_entity = hero_location.distance(obj.get_location())
            if not self.poll_step in self.metadata.encounters:
                self.metadata.encounters[self.poll_step] = []
            self.metadata.encounters[self.poll_step].append(encounter)

    # Equivalent to load scenario, but for replay metadata files
    def load_replay(self, replay_metadata_file_path):
        print("Loading replay metadata " + replay_metadata_file_path)
        metadata_reader = RemoMetadataReader(replay_metadata_file_path)
        self.metadata = metadata_reader.read()
        print(self.metadata.ego_id)
        print("Loading replay file", self.metadata.replay_file)
        self.client.set_replayer_ignore_hero(False)
        self.client.set_replayer_ignore_spectator(False)
        self.client.replay_file(self.metadata.replay_file, 0, 20, self.metadata.ego_id)        
        
    def play_replay(self):
        self.main_loop()

    def main_loop(self):
        while self.is_running:
            self.world.tick()

    def get_hero(self):
        actors = self.world.get_actors()
        if self.metadata.ego_id == None:
            for actor in actors:
                if "role_name" in actor.attributes.keys():
                    if actor.attributes["role_name"] == "hero":
                        print("Got hero id " + str(actor.id))
                        self.active_hero_id = int(actor.id)
                        self.metadata.ego_id = self.active_hero_id
        print(self.world.get_actor(self.metadata.ego_id))
        return self.world.get_actor(self.metadata.ego_id)
    
    def get_hero_location(self):
        return self.get_hero().get_location()
    
    def replace_hero(self):
        transform = self.get_hero().get_transform()
        self.get_hero().set_location(carla.Location(10000, 10000, 10000))
        time.sleep(0.05)
        self.get_hero().destroy()
        blueprint_library = self.world.get_blueprint_library()
        vehicle_bp = random.choice(blueprint_library.filter('vehicle.*.*'))
        vehicle_bp.set_attribute("role_name", "hero")
        actor = self.world.spawn_actor(vehicle_bp, transform)
        print(actor.attributes)
        self.metadata.ego_id = actor.id
        self.active_hero_id = actor.id
        print("New hero id is " + str(actor.id))

    def get_actors(self):
        return self.world.get_actors()

    def get_environment_objects(self):
        return self.world.get_environment_objects()

    def disable_environment_objects(self, ids):
        self.world.enable_environment_objects(ids, False)

    def enable_environment_objects(self, ids):
        self.world.enable_environment_objects(ids, True)

    def toggle_daytime(self):
        if self.is_day:
            self.set_night()
        else:
            self.set_day()

    def toggle_wet_dry(self):
        weather = self.world.get_weather()
        if weather.wetness > 50:
            self.set_dry()
        else:
            self.set_wet()

    def toggle_fog(self):
        if self.is_foggy:
            self.disable_fog()
        else:
            self.enable_fog()

    def enable_fog(self):
        weather = self.world.get_weather()
        weather.fog_density = 80
        weather.fog_distance = 10
        self.world.set_weather(weather)

    def disable_fog(self):
        weather = self.world.get_weather()
        weather.fog_density = 0
        weather.fog_distance = 1000000
        self.world.set_weather(weather)

    def set_day(self):
        weather = self.world.get_weather()
        weather.sun_altitude_angle = 70
        self.world.set_weather(weather)

    def set_night(self):
        weather = self.world.get_weather()
        weather.sun_altitude_angle = -90
        self.world.set_weather(weather)

    def set_wet(self):
        weather = self.world.get_weather()
        weather.wetness = 80
        self.world.set_weather(weather)

    def set_dry(self):
        weather = self.world.get_weather()
        weather.wetness = 0
        self.world.set_weather(weather)

    def add_label(self, location, text):
        self.world.debug.draw_string(location, text, life_time=200)
        
    def get_objects_within_radius(self, location, radius):
        actors = [actor for actor in self.get_actors() if location.distance(actor.get_location()) <= radius]
        env_objects = [obj for obj in self.get_environment_objects() if location.distance(obj.transform.location) <= radius]
        return (actors, env_objects)

    def display_ids_within_radius(self, location, radius):
        actors, env_objects = self.get_objects_within_radius(location, radius)

        for actor in actors:
            self.add_label(actor.get_location(), "Actor: " + str(actor.id))

        for obj in env_objects:
            self.add_label(obj.bounding_box.location, "Environment Object: " + str(obj.id))
            
    def filter_objects(self, objects, obj_type):
        return [obj for obj in objects if str(obj.type) == obj_type]
            
