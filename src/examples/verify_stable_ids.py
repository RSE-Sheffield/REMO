import carla
from remo.remo_api import RemoAPI

# Instantiate the API object
remoAPI = RemoAPI()

# Connect to the server
remoAPI.connect_to_server()

# Load the replay file
remoAPI.load_replay("default-metadata-path.json")

search_location = carla.Location(0.0, 0.0, 0.0)
search_radius = 10.0
actors, objects = remoAPI.get_objects_within_radius(search_location, search_radius)
print("All objects:")
    
for object in objects:
    print(str(object.id) + ", " + str(object.type))
    
# Repeat fifty times and check the ids are the same
for i in range(0,50):
    # Load the replay file
    remoAPI.load_replay("default-metadata-path.json")
    new_actors, new_objects = remoAPI.get_objects_within_radius(search_location, search_radius)
    
    for i in range(0, len(objects)-1):
        assert(objects[i].id == new_objects[i].id)
        
print("Verified ids are consistent")
    