import carla
from remo.remo_api import RemoAPI

# Instantiate the API object
remoAPI = RemoAPI()

# Connect to the server
remoAPI.connect_to_server()

search_location = carla.Location(0.0, 0.0, 0.0)
search_radius = 10.0
actors, objects = remoAPI.get_objects_within_radius(search_location, search_radius)
print("All objects:")
for object in objects:
    print(str(object.id) + ", " + str(object.type))
    
# Only get poles
print("Only poles:")
poles = remoAPI.filter_objects_by_type(objects, "Poles")
for object in poles:
    print(str(object.id) + ", " + str(object.type))