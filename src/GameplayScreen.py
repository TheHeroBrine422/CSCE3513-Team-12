import tkinter as tk

class GameplayScreen(tk.Frame):
    # Hex codes for colors
    PURPLE = '#4f62c4'
    RED = '#450c19'
    GREEN = '#093b15'
    GRAY = "#222222"
    WHITE = "#d9d9d9"

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='black')
        self.controller = controller
        self.red_team = []
        self.green_team = []

        # Create frame for player scores on top of screen
        score_frame = tk.Frame(self, bg=self.GRAY)
        score_frame.pack(side=tk.TOP)

        # Create frame for each team
        self.red_team_frame = tk.Frame(score_frame, bd=2, relief=tk.GROOVE, bg=self.RED)
        self.red_team_frame.pack(side=tk.LEFT, padx=10, pady=5, anchor="n")

        self.green_team_frame = tk.Frame(score_frame, bd=2, relief=tk.GROOVE, bg=self.GREEN)
        self.green_team_frame.pack(side=tk.LEFT, padx=10, pady=5, anchor="n")

        # Create labels for the Red and Green Teams
        red_team_label = tk.Label(self.red_team_frame, text="RED TEAM", font=("Helvetica", 16), bg=self.RED, fg=self.WHITE)
        red_team_label.pack()

        green_team_label = tk.Label(self.green_team_frame, text="GREEN TEAM", font=("Helvetica", 16), bg=self.GREEN, fg=self.WHITE)
        green_team_label.pack()

        # Create frames for the tables of the Red and Green Teams
        self.red_table_frame = tk.Frame(self.red_team_frame, bg=self.RED)
        self.red_table_frame.pack()

        self.green_table_frame = tk.Frame(self.green_team_frame, bg=self.GREEN)
        self.green_table_frame.pack()

    def set_teams(self, red, green):
        self.red_team = red
        self.green_team = green
        self.red_rows = []
        self.green_rows = []

        for i in range(0, len(self.red_team)):
            player_name = tk.Label(self.red_table_frame, text=self.red_team[i].name, anchor="w", bg=self.RED, fg=self.WHITE)
            player_name.grid(row=i, column=0, padx=(5, 0), pady=5)

            player_score = tk.Label(self.red_table_frame, text=self.red_team[i].score, anchor="e", bg=self.RED, fg=self.WHITE)
            player_score.grid(row=i, column=1, padx=(5, 0), pady=5)

            self.red_rows.append([player_name, player_score])
        
        # Center the Red Team table
        self.red_table_frame.pack(side=tk.TOP, pady=5)

        for i in range(0, len(self.green_team)):
            player_name = tk.Label(self.green_table_frame, text=self.green_team[i].name, anchor="w", bg=self.GREEN, fg=self.WHITE)
            player_name.grid(row=i, column=0, padx=(5, 0), pady=5)

            player_score = tk.Label(self.green_table_frame, text=self.green_team[i].score, anchor="e", bg=self.GREEN, fg=self.WHITE)
            player_score.grid(row=i, column=1, padx=(5, 0), pady=5)

            self.green_rows.append([player_name, player_score])
        
        # Center the Green Team table
        self.green_table_frame.pack(side=tk.TOP, pady=5)