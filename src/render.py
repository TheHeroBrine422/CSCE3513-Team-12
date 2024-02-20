import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

class RenderingManager(tk.Tk):
    def __init__(self, gameState, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.gameState = gameState
        #self.networkingManager = networkingManager
        #self.databaseManager = databaseManager
        self.title("rendering...")
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
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (SplashScreen, PlayerEntry):
            frame = F(container, self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            #frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(SplashScreen)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()

    def tick(self):
        # do actual rendering here.
        pass

class SplashScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Add image file 
        #SCREEN_WIDTH = parent.winfo_width()
        #SCREEN_HEIGHT = parent.winfo_height()
        parent.bg = bg = PhotoImage(file = r'src/icons/logo.png')
        parent.bg = bg = bg.subsample(2,2)
        #parent.bg = bg = Image.open(r'src/icons/logo.png')
        #parent.bg = bg = bg.resize(SCREEN_WIDTH, SCREEN_HEIGHT)
  
        # Create Canvas 
        canvas1 = Canvas(parent, width = SCREEN_WIDTH, height = SCREEN_HEIGHT) 
  
        canvas1.pack(fill = "both", expand = True) 
  
        # Display image 
        print("screenheight:", SCREEN_HEIGHT)
        print("screenwidth:", SCREEN_WIDTH)
        canvas1.create_image((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2), image = bg, anchor = CENTER) 
        label = tk.Label(self, text="Splash Screen")
        label.pack(padx=10, pady=10)

class PlayerEntry(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Player Entry")
        label.pack(padx=10, pady=10)