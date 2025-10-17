import customtkinter
from threading import Timer
import subprocess
import time

class RemoRecordScenarioTab(customtkinter.CTkFrame):
    def __init__(self, master, remoAPI, **kwargs):
        super().__init__(master, **kwargs)
        
        # Set remoAPI object
        self.remoAPI = remoAPI
        
        # ADS selector
        self.ads_label = customtkinter.CTkLabel(self, text="Select ADS: ")
        self.ads_label.grid(row=0, column=0, padx=10, pady=10)

        self.ads_combo = customtkinter.CTkComboBox(self, values=['Manual', 'Transfuser++'])
        self.ads_combo.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        
        # Scenario Selector
        self.scenario_button = customtkinter.CTkButton(self, text="Select Scenario", command=self.choose_scenario_file)
        self.scenario_button.grid(row=1, column=0, padx=10, pady=10)
        
        self.scenario_path_entry = customtkinter.CTkEntry(self, placeholder_text="Enter scenario path...", width=600)
        self.scenario_path_entry.grid(row=1, column=1, padx=10, pady=10)
        
        # Recording end options

        self.record_for_label = customtkinter.CTkLabel(self, text="Record for (s)")
        self.record_for_label.grid(row=2, column=0, padx=10, pady=10)
        
        self.record_for_path_entry = customtkinter.CTkEntry(self, placeholder_text="Enter max recording time in seconds...", width=300)
        self.record_for_path_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.break_on_crash_checkbox = customtkinter.CTkCheckBox(master=self, text="Stop Recording on Crash")
        self.break_on_crash_checkbox.grid(row=3, column=0, padx=10, pady=10)
        
        # Start button
        self.start_recording_button = customtkinter.CTkButton(self, text="Start Recording", command=self.start_recording)
        self.start_recording_button.grid(row=4, column=0, padx=10, pady=10)
        
        
    def choose_scenario_file(self):
        filename = customtkinter.filedialog.askopenfilename()
        self.scenario_path_entry.insert(-1, filename)
        
    def start_recording(self):
        print("Loading scenario " + self.scenario_path_entry.get())
        subprocess.Popen(["python3", self.scenario_path_entry.get()])
        time.sleep(3)
        subprocess.Popen(["python3", "/atlas/RSE/carla_server/PythonAPI/examples/manual_control.py"])
        time.sleep(3)
        print("Scenario loaded")
        self.remoAPI.start_recording() 
        t = Timer(20.0, self.stop_recording)
        t.start()
    
    def stop_recording(self):
        self.remoAPI.stop_recording()

def ads_combo_callback():
    print("ADS Combo callback not yet implemented!")
    