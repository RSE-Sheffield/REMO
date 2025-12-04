from remo.remo_api import RemoAPI
import remo.carla_helpers.server

# Instantiate the API object
remoAPI = RemoAPI()

# Launch the server
remo.carla_helpers.server.launch_carla_server()
