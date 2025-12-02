import time
from remo.remo_api import RemoAPI
from remo.remo_scenario_config import RemoScenarioConfiguration
from remo.remo_recording_config import RemoRecordingConfig

# Instantiate the API object
remoAPI = RemoAPI()

# Connect to the server
remoAPI.connect_to_server()

# Prepare the initial scenario
scenario_config = RemoScenarioConfiguration()
scenario_config.scenario_file = "FollowLeadingVehicle_1"
remoAPI.load_scenario(scenario_config)

# Allow time for the scenario to load
time.sleep(5.0)

# Prepare the recording config
recording_config = RemoRecordingConfig()

# Run the scenario
remoAPI.run_active_scenario(recording_config)

# We could now load the replay file
remoAPI.load_replay("default-metadata-path.json")

# Make some changes
remoAPI.set_dry()
remoAPI.replace_hero()

# Spawn the new ego vehicle here
remoAPI.load_manual_control()


