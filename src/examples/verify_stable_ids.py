import carla
from remo.remo_api import RemoAPI

# Instantiate the API object
remoAPI = RemoAPI()

# Connect to the server
remoAPI.connect_to_server()

# Load the replay file
remoAPI.load_replay("default-metadata-path.json")

search_location = carla.Location(0.0, 0.0, 0.0)
search_radius = 500.0
actors, objects = remoAPI.get_objects_within_radius(search_location, search_radius)
sorted_actors = sorted(actors, key=lambda actor: actor.id, reverse=True)

print("Comparing " + str(len(objects)) + " objects and " + str(len(actors)) + " actors")

# Repeat fifty times and check the ids are the same
for i in range(0, 50):
    # Load the replay file
    remoAPI.load_replay("default-metadata-path.json")
    
    # Grab the actors and objects
    new_actors, new_objects = remoAPI.get_objects_within_radius(search_location, search_radius)
    
    # Ensure actors are sorted by ID
    sorted_new_actors = sorted(new_actors, key=lambda actor: actor.id, reverse=True)

    # Check we have the correct number of objects & actors
    assert(len(sorted_actors) == len(sorted_new_actors))
    assert(len(objects) == len(new_objects))

    # Check the objects have the same IDs
    for i in range(0, len(objects)-1):
        assert(objects[i].id == new_objects[i].id)
        
    # Check actors have the same ID, type and transform
    for i in range(0, len(actors)-1): 
        assert(sorted_actors[i].id == sorted_new_actors[i].id and 
               sorted_actors[i].type_id == sorted_new_actors[i].type_id and 
               sorted_actors[i].get_transform() == sorted_new_actors[i].get_transform())

print("Verified ids are consistent")
