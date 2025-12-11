from remo.remo_api import RemoAPI
from threading import Timer

# Instantiate the API object
remoAPI = RemoAPI()

# Connect to the server
remoAPI.connect_to_server()

remoAPI.pause()

# We could now load the replay file
remoAPI.load_replay("default-metadata-path.json")

# Make some changes
remoAPI.set_dry()
remoAPI.replace_ego_vehicle()

# Spawn the new ego vehicle here
remoAPI.load_manual_control()

remoAPI.play()

t = Timer(15.0, remoAPI.pause)
t.start()