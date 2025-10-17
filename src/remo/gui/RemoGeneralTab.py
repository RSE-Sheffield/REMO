import customtkinter
import remo.carla_helpers.server

class RemoGeneralTab(customtkinter.CTkFrame):
    def __init__(self, master, remoAPI, **kwargs):
        super().__init__(master, **kwargs)
        
        # Set remoAPI object
        self.remoAPI = remoAPI

        # Add Start Carla button
        self.start_carla_button = customtkinter.CTkButton(master=self, text="Start Carla", command=remo.carla_helpers.server.launch_carla_server)
        self.start_carla_button.grid(row=0, column=0, padx=20, pady=10)
        
        # Add connect to server button
        self.connect_button = customtkinter.CTkButton(master=self, text="Connect to server", command=self.remoAPI.connect_to_server)
        self.connect_button.grid(row=1, column=0, padx=20, pady=10)
        