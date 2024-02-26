import tkinter as tk

class EntryScreen(tk.Frame):
    def __init__(self, parent, controller):

        self.controller = controller

        # Hex codes for colors
        self.PURPLE = '#4f62c4'
        self.RED = '#450c19'
        self.GREEN = '#093b15'
        self.GRAY = "#222222"
        self.WHITE = "#d9d9d9"

        self.red_team = [] # todo: this data should *probably* be part of the gameState variable which is passed from main to render, but not to this class, for now im just doing it like this though.
        self.green_team = []
        for _ in range(15):
            self.red_team.append({"uniqueID": -1, "codename": "", "equipmentID": -1})
            self.green_team.append({"uniqueID": -1, "codename": "", "equipmentID": -1})


        tk.Frame.__init__(self, parent, bg=self.GRAY)

        # Create a header label
        header_label = tk.Label(self, text="Edit Current Game", font=("Helvetica", 20, "bold"), fg = self.PURPLE, bg=self.GRAY)
        header_label.pack(side=tk.TOP, pady=10)

        # Create 8 buttons
        buttons_frame = tk.Frame(self, bg=self.GRAY)
        buttons_frame.pack(side=tk.BOTTOM, pady=10)

        buttons = []
        labels = [
            "Edit Game",
            "Game Parameters",
            "Start Game",
            "PreEntered Games",
            "",
            "View Game",
            "Flick Sync",
            "Clear Game"
        ]
        for i, label in enumerate(labels, start=1):
            # Use function key labels (F1, F2, ..., F8) along with the specified labels
            button = tk.Button(buttons_frame, text=f"F{i}\n{label}", command=lambda i=i: self.on_button_click(i))
            button.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)
            buttons.append(button)

        # Bind all key events globally
        self.master.bind_all("<KeyPress>", self.on_key_press)

        # Create frames for the Red and Green Teams, encapsulate them in another frame
        teams_frame = tk.Frame(self, bg=self.GRAY)
        teams_frame.pack(side=tk.TOP)

        self.red_team_frame = tk.Frame(teams_frame, bd=2, relief=tk.GROOVE, bg=self.RED)
        self.red_team_frame.pack(side=tk.LEFT, padx=10, pady=5, anchor="n")

        self.green_team_frame = tk.Frame(teams_frame, bd=2, relief=tk.GROOVE, bg=self.GREEN)
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

        # Create 15x2 tables with Entry widgets and row numbers for the Red Team
        column1_label_red = tk.Label(self.red_table_frame, text="Unique ID", width=8, anchor="w", bg=self.RED, fg=self.WHITE)
        column1_label_red.grid(row=0, column=1, padx=(5, 0), pady=5)

        column2_label_red = tk.Label(self.red_table_frame, text="Codename", width=8, anchor="w", bg=self.RED, fg=self.WHITE)
        column2_label_red.grid(row=0, column=2, padx=(5, 0), pady=5)

        column2_label_red = tk.Label(self.red_table_frame, text="Equipment ID", width=11, anchor="w", bg=self.RED, fg=self.WHITE)
        column2_label_red.grid(row=0, column=3, padx=(5, 0), pady=5)

        entries_red = []
        for i in range(1, 16):
            row_label = tk.Label(self.red_table_frame, text=f"{i + 1}.", width=3, anchor="w", bg=self.RED, fg=self.WHITE)
            row_label.grid(row=i, column=0, padx=(5, 0), pady=5)

            row_entries = []
            for j in range(1, 4):
                entry = tk.Entry(self.red_table_frame, width=20, bg=self.WHITE, fg="black")
                entry.grid(row=i, column=j, padx=5, pady=5)
                entry.bind("<FocusOut>", lambda event, row=i, col=j, entry=entry: self.on_entry_change(event, row, col, entry, 'red'))
                row_entries.append(entry)
            entries_red.append(row_entries)

        # Center the Red Team table
        self.red_table_frame.pack(side=tk.TOP, pady=5)

        column1_label_green = tk.Label(self.green_table_frame, text="Unique ID", width=8, anchor="w", bg=self.GREEN, fg=self.WHITE)
        column1_label_green.grid(row=0, column=1, padx=(5, 0), pady=5)

        column2_label_green = tk.Label(self.green_table_frame, text="Codename", width=8, anchor="w", bg=self.GREEN, fg=self.WHITE)
        column2_label_green.grid(row=0, column=2, padx=(5, 0), pady=5)

        column3_label_green = tk.Label(self.green_table_frame, text="Equipment ID", width=11, anchor="w", bg=self.GREEN, fg=self.WHITE)
        column3_label_green.grid(row=0, column=3, padx=(5, 0), pady=5)

        # Create 15x2 tables with Entry widgets and row numbers for the Green Team
        entries_green = []
        for i in range(1, 16):
            row_label = tk.Label(self.green_table_frame, text=f"{i + 1}.", width=3, anchor="w", bg=self.GREEN, fg=self.WHITE)
            row_label.grid(row=i, column=0, padx=(5, 0), pady=5)

            row_entries = []
            for j in range(1, 4):
                entry = tk.Entry(self.green_table_frame, width=20, bg=self.WHITE, fg="black")
                entry.grid(row=i, column=j, padx=5, pady=5)
                entry.bind("<FocusOut>", lambda event, row=i, col=j, entry=entry: self.on_entry_change(event, row, col, entry, 'green'))
                row_entries.append(entry)
            entries_green.append(row_entries)

        # Center the Green Team table
        self.green_table_frame.pack(side=tk.TOP, pady=5)

    def on_button_click(self, button_number):
        print(f"Button {button_number} clicked!")

    def on_key_press(self, event):
        # Check if the pressed key is a function key (F1, F2, ..., F8)
        if event.keysym.startswith("F") and event.keysym[1:].isdigit():
            button_number = int(event.keysym[1:])
            self.on_button_click(button_number)

    # Function to handle changes in the Entry widgets
    def on_entry_change(self, event, row, col, entry, team):
        value = entry.get().strip()
        if value == "":
            return


        if col == 1:
            codename = self.controller.databaseManager.getPlayer(value)
            self.red_team[row - 1]["uniqueID"] = codename
            if team == 'red':
                self.red_team[row-1]["uniqueID"] = value
                if codename is not None:
                    codenameLabel = tk.Label(self.red_table_frame, text=codename, width=20, anchor="w", bg=self.RED, fg=self.WHITE)
                    codenameLabel.grid(row=row, column=2, padx=(5, 0), pady=5)
            if team == 'green':
                self.red_team[row - 1]["uniqueID"] = value
                if codename is not None:
                    codenameLabel = tk.Label(self.green_team_frame, text=codename, width=20, anchor="w", bg=self.GREEN, fg=self.WHITE)
                    codenameLabel.grid(row=row, column=2, padx=(5, 0), pady=5)
        elif col == 2:
            self.tempUniqueID = "" # dealing with weird local variable issue.
            if team == 'red':
                self.red_team[row - 1]["codename"] = value
                self.tempUniqueID = self.red_team[row - 1]["uniqueID"]
            else:
                self.green_team[row - 1]["codename"] = value
                self.tempUniqueID = self.green_team[row - 1]["uniqueID"]
            self.controller.databaseManager.addPlayer(self.tempUniqueID, value)
        elif col == 3:
            if team == 'red':
                self.red_team[row - 1]["equipmentID"] = value
            else:
                self.green_team[row - 1]["equipmentID"] = value
            self.controller.networkingManager.send_broadcast(value)

        print(f"Value in row {row}, column {col} changed to: {value}")
