""" Main module """

import carla
from remo.remo_api import RemoAPI
from remo.gui.RemoApp import RemoApp

app = RemoApp()
app.mainloop()

#remoAPI = RemoAPI()
#remoAPI.toggle_daytime()
#remoAPI.display_ids_within_radius(carla.Location(0, 0, 0), 50)
