import tkinter as tk
from tkinter import *
import SplashScreen

class RenderingManager(tk.Tk):
    def __init__(self, gameState, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.gameState = gameState
        #self.networkingManager = networkingManager
        #self.databaseManager = databaseManager
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
        self.frames["SplashScreen"] = SplashScreen.SplashScreen(container, self)
        self.frames["SplashScreen"].grid(row=0, column=0, sticky="nsew")

        #Enter PlayerEntry into frames dictionary
        self.frames["PlayerEntry"] = PlayerEntry(container, self)
        self.frames["PlayerEntry"].grid(row=0, column=0, sticky="nsew")

        # Set first frame
        self.show_frame("SplashScreen")

    def show_frame(self, cont):
        # select frame to show
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()

    def tick(self):
        # do actual rendering here.
        self.update()
        pass


class PlayerEntry(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        label = tk.Label(self, text="Player Entry")
        label.grid()