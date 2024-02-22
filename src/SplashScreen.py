import tkinter as tk
from tkinter import *

class SplashScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="black")

        # Create grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
  
        # Get image
        parent.bg = bg = PhotoImage(file = r'src/icons/logo.png')
        # Resize image
        parent.bg = bg = bg.subsample(2,2)
        # Add image to Label
        logo_label = Label(self, image = bg)
        # Place Label in frame's grid
        logo_label.grid()

        # switch to EntryScreen frame after 5 seconds
        parent.after(3000, controller.show_frame, "EntryScreen")