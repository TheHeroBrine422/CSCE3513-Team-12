import tkinter as tk
from tkinter.font import BOLD, Font
from Player import Player

class GameplayScreen(tk.Frame):
    # Hex codes for colors
    PURPLE = '#4f62c4'
    RED = '#450c19'
    GREEN = '#093b15'
    GRAY = "#222222"
    WHITE = "#d9d9d9"

    def __init__(self, parent, controller, model):
        tk.Frame.__init__(self, parent, bg='black')
        self.controller = controller
        self.model = model
        self.red_team = [] # list of Player objects
        self.green_team = [] # list of Player objects

        self.HEADER_FONT = Font(self.controller, family='Helvetica', size=48, weight='bold')
        self.PLAYER_FONT = Font(self.controller, family='Helvetica', size=24, weight='bold')
        self.SCORE_FONT = Font(self.controller, family='Helvetica', size=24)

        # Create frame for player scores on top of screen
        score_frame = tk.Frame(self, bg='black')
        score_frame.pack(side=tk.TOP, fill='both', expand=True)

        # Create frame for player SCROLL on BOTTOM of screen
        scroll_frame = tk.Frame(self, bg=self.GRAY)
        scroll_frame.pack(side='bottom', fill='both', expand=True)

        # Create frame for each team
        self.red_team_frame = tk.Frame(score_frame, bd=2, relief=tk.GROOVE, bg=self.WHITE)
        self.red_team_frame.pack(side='left', padx=10, pady=5, anchor="n", fill='both', expand=True)

        self.green_team_frame = tk.Frame(score_frame, bd=2, relief=tk.GROOVE, bg=self.WHITE)
        self.green_team_frame.pack(side='left', padx=10, pady=5, anchor="n", fill='both', expand=True)

        # Create labels for the Red and Green Teams
        red_team_label = tk.Label(self.red_team_frame, text="RED TEAM", font=self.HEADER_FONT, bg=self.WHITE, fg=self.RED)
        red_team_label.pack()

        green_team_label = tk.Label(self.green_team_frame, text="GREEN TEAM", font=self.HEADER_FONT, bg=self.WHITE, fg=self.GREEN)
        green_team_label.pack()

        # Create frames for the tables of the Red and Green Teams
        self.red_table_frame = tk.Frame(self.red_team_frame, bg=self.WHITE)
        self.red_table_frame.pack(side='left', padx=10, pady=5, anchor='n', fill='both', expand=True)
        self.red_table_frame.grid_columnconfigure(0, weight=2)
        self.red_table_frame.grid_columnconfigure(1, weight=1)

        self.green_table_frame = tk.Frame(self.green_team_frame, bg=self.WHITE)
        self.green_table_frame.pack(side='left', padx=10, pady=5, anchor='n', fill='both', expand=True)
        self.green_table_frame.grid_columnconfigure(0, weight=2)
        self.green_table_frame.grid_columnconfigure(1, weight=1)

    def set_teams(self, red, green):
        self.red_team = red # list of Players
        self.green_team = green # list of Players
        self.red_rows = [] # list of lists of Labels
        self.green_rows = [] # list of lists of Labels

        for i in range(0, len(self.red_team)):
            player_name = tk.Label(self.red_table_frame, text=self.red_team[i].name, anchor='w', bg=self.WHITE, fg=self.RED, font=self.PLAYER_FONT)
            player_name.grid(row=i, column=0, padx=(5, 0), pady=5, sticky='w')

            player_score = tk.Label(self.red_table_frame, text=self.red_team[i].score, anchor='e', bg=self.WHITE, fg=self.RED, font=self.SCORE_FONT)
            player_score.grid(row=i, column=1, padx=(5, 0), pady=5, sticky='e')

            self.red_rows.append([player_name, player_score])
        
        # Center the Red Team table
        self.red_table_frame.pack(side=tk.TOP, pady=5, fill='both', expand=True)

        for i in range(0, len(self.green_team)):
            player_name = tk.Label(self.green_table_frame, text=self.green_team[i].name, anchor='w', bg=self.WHITE, fg=self.GREEN, font=self.PLAYER_FONT)
            player_name.grid(row=i, column=0, padx=(5, 0), pady=5, sticky='w')

            player_score = tk.Label(self.green_table_frame, text=self.green_team[i].score, anchor='e', bg=self.WHITE, fg=self.GREEN, font=self.SCORE_FONT)
            player_score.grid(row=i, column=1, padx=(5, 0), pady=5, sticky='e')

            self.green_rows.append([player_name, player_score])
        
        # Center the Green Team table
        self.green_table_frame.pack(side=tk.TOP, pady=5, fill='both', expand=True)