import customtkinter

from .RemoGeneralTab import RemoGeneralTab
from .RemoRecordScenarioTab import RemoRecordScenarioTab
from .RemoReplayTab import RemoReplayTab

class RemoMainTabView(customtkinter.CTkTabview):
    def __init__(self, master, remoAPI, **kwargs):
        super().__init__(master, **kwargs)
        
        # Set remoAPI object
        self.remoAPI = remoAPI

        # Create General tab
        self.general_tab = self.add("General")
        self.general_tab = RemoGeneralTab(master=self.tab("General"), remoAPI=self.remoAPI)
        self.general_tab.grid(row=0, column=0, padx=10, pady=0)
        
        # Create Record Scenario tab
        self.record_tab = self.add("Record Scenario")
        self.record_tab = RemoRecordScenarioTab(master=self.tab("Record Scenario"), remoAPI=self.remoAPI)
        self.record_tab.grid(row=0, column=0, padx=10, pady=0)
        
        # Create Replay with Modifcation tab
        self.replay_tab = self.add("Replay with Modification")
        self.replay_tab = RemoReplayTab(master=self.tab("Replay with Modification"), remoAPI=self.remoAPI)
        self.replay_tab.grid(row=0, column=0, padx=10, pady=0)
        
        # Styling
        self._segmented_button.grid(sticky="W")
