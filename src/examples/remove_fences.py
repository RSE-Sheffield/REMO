from remo.remo_api import RemoAPI

# Instantiate the API object
remoAPI = RemoAPI()

# Connect to the server
remoAPI.connect_to_server()

# We could now load the replay file
remoAPI.load_replay("default-metadata-path.json")

# Remove fences within 50 units of the ego vehicle's initial location
search_location = remoAPI.get_ego_vehicle_location()
search_radius = 50.0
actors, objects = remoAPI.get_objects_within_radius(search_location, search_radius)
fences = remoAPI.filter_objects_by_type(objects, "Fences")
fence_ids = [fence.id for fence in fences]
remoAPI.disable_environment_objects(fence_ids)


