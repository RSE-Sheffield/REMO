import customtkinter
from .RemoMainTabView import RemoMainTabView
from remo.remo_api import RemoAPI

class RemoApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("REMO")
        self.geometry("1000x800")
        self.remoAPI = RemoAPI()
        self.main_tab_view = RemoMainTabView(master=self, remoAPI=self.remoAPI)
        self.main_tab_view.pack(side="top", fill="both")
