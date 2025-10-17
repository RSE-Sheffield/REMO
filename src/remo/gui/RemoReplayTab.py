import customtkinter
import subprocess
import time
import remo.carla_helpers.server

class RemoReplayTab(customtkinter.CTkFrame):
    def __init__(self, master, remoAPI, **kwargs):
        super().__init__(master, **kwargs)
        
        self.remoAPI = remoAPI
        
        # Ego vehicle ID entry
        self.hero_id_entry = customtkinter.CTkEntry(self, placeholder_text="Enter ego ID...", width=600)
        self.hero_id_entry.grid(row=1, column=1, padx=10, pady=10)
        
        # Replay button
        self.replay_button = customtkinter.CTkButton(self, text="Replay without ego", command=self.replay_without_hero)
        self.replay_button.grid(row=1, column=0, padx=10, pady=10)

    def replay_without_hero(self):
        self.remoAPI.client.replay_file("test-log.log", 0, 20, int(self.hero_id_entry.get()))        
        hero = self.remoAPI.get_hero(int(self.hero_id_entry.get()))
        print("Hero is ")
        print(hero)
        loc = hero.get_location()
        print(loc)
        self.remoAPI.remove_hero(int(self.hero_id_entry.get()))
        #subprocess.Popen(["python3", "/atlas/RSE/carla_server/PythonAPI/examples/manual_control.py", "--xpos", str(loc.x), "--ypos", str(loc.y), "--zpos", str(loc.z)])
        #time.sleep(3)