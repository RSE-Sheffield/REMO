from remo.remo_api import RemoAPI

# Instantiate the API object
remoAPI = RemoAPI()

# Connect to the server
remoAPI.connect_to_server()

# We could now load the replay file
remoAPI.load_replay("default-metadata-path.json")

# Make some changes
remoAPI.set_dry()
remoAPI.replace_hero()

# Spawn the new ego vehicle here
remoAPI.load_manual_control()

