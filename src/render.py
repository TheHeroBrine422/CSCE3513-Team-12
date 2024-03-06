import tkinter as tk
from tkinter import *
from SplashScreen import SplashScreen
from EntryScreen import EntryScreen
from GameplayScreen import GameplayScreen
from GameplayModel import GameplayModel

class RenderingManager(tk.Tk):
    def __init__(self, gameState, gameplayModel, networkingManager, databaseManager, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.gameState = gameState
        self.networkingManager = networkingManager
        self.gameplayModel = gameplayModel
        self.databaseManager = databaseManager
        self.title("Proton Laser Tag")
        global SCREEN_HEIGHT
        global SCREEN_WIDTH
        SCREEN_WIDTH = self.winfo_screenwidth()               
        SCREEN_HEIGHT = self.winfo_screenheight()               
        self.geometry("%dx%d" % (SCREEN_WIDTH, SCREEN_HEIGHT))

        # creating a frame and assigning it to container
        container = tk.Frame(self, height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
        # specifying the region where the frame is packed in root
        container.pack(side="top", fill="both", expand=True)

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}

        # Enter SplashScreen into frames dictionary
        self.frames["SplashScreen"] = SplashScreen(container, self)
        self.frames["SplashScreen"].grid(row=0, column=0, sticky="nsew")

        #Enter EntryScreen into frames dictionary
        self.frames["EntryScreen"] = EntryScreen(container, self)
        self.frames["EntryScreen"].grid(row=0, column=0, sticky="nsew")

        #Enter GameplayScreen into frames dictionary
        self.frames["GameplayScreen"] = GameplayScreen(container, self, self.gameplayModel)
        self.frames["GameplayScreen"].grid(row=0, column=0, sticky="nsew")
        self.gameplayModel.set_screen(self.frames["GameplayScreen"])

        # Set first frame
        self.show_frame("SplashScreen")

    def show_frame(self, cont):
        # select frame to show
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()

    def get_frame(self, name):
        return self.frames[name]
    
    def change_game_state(self, state):
        self.gameState["stage"] = state
        self.networkingManager.gameState["stage"] = state
        self.databaseManager.gameState["stage"] = state

    def set_model_teams(self, green_team, red_team):
        self.gameplayModel.set_teams(green_team, red_team)

    def tick(self):
        # do actual rendering here.
        self.update()