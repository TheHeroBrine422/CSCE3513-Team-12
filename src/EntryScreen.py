import tkinter as tk
from Player import Player
from Stage import Stage

class EntryScreen(tk.Frame):
    def __init__(self, parent, controller):

        self.controller = controller
        self.TEAM_SIZE = 15

        # Hex codes for colors
        self.PURPLE = '#4f62c4'
        self.RED = '#450c19'
        self.GREEN = '#093b15'
        self.GRAY = "#222222"
        self.WHITE = "#d9d9d9"

        tk.Frame.__init__(self, parent, bg=self.GRAY)

        # Create a header label
        header_label = tk.Label(self, text="Edit Current Game", font=("Helvetica", 20, "bold"), fg = self.PURPLE, bg=self.GRAY)
        header_label.pack(side=tk.TOP, pady=10)

        # Create 8 buttons
        buttons_frame = tk.Frame(self, bg=self.GRAY)
        buttons_frame.pack(side=tk.BOTTOM, pady=10)

        buttons = []
        labels = [
            "",
            "",
            "",
            "",
            "Start Game",
            "",
            "",
            "Clear Players"
        ]
        for i, label in enumerate(labels, start=1):
            # Use function key labels (F1, F2, ..., F8) along with the specified labels
            button = tk.Button(buttons_frame, text=f"F{i}\n{label}", command=lambda i=i: self.on_button_click(i))
            button.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)
            buttons.append(button)

        # Bind all key events globally
        self.master.bind_all("<KeyPress>", self.on_key_press)
        buttons[4].config(command=self.start_game)
        buttons[7].config(command=self.clear_entries)

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
        column1_label_red = tk.Label(self.red_table_frame, text="Unique ID", font=("Helvetica", 15), width=8, anchor="w", bg=self.RED, fg=self.WHITE)
        column1_label_red.grid(row=0, column=1, padx=(5, 0), pady=5)

        column2_label_red = tk.Label(self.red_table_frame, text="Codename", font=("Helvetica", 15), width=8, anchor="w", bg=self.RED, fg=self.WHITE)
        column2_label_red.grid(row=0, column=2, padx=(5, 0), pady=5)

        column2_label_red = tk.Label(self.red_table_frame, text="Equipment ID", font=("Helvetica", 15), width=11, anchor="w", bg=self.RED, fg=self.WHITE)
        column2_label_red.grid(row=0, column=3, padx=(5, 0), pady=5)

        self.entries_red = []
        for i in range(1, self.TEAM_SIZE + 1):
            row_label = tk.Label(self.red_table_frame, text=f"{i}.", font = ("Helvetica", 15), width=3, anchor="w", bg=self.RED, fg=self.WHITE)
            row_label.grid(row=i, column=0, padx=(5, 0), pady=5)

            row_entries = []
            for j in range(1, 4):
                entry = tk.Entry(self.red_table_frame, font=("Helvetica", 15), width=20, bg=self.WHITE, fg="black")
                entry.grid(row=i, column=j, padx=5, pady=3)
                entry.bind("<FocusOut>", lambda event, row=i, col=j, entry=entry: self.on_entry_change(event, row, col, entry, 'red'))
                row_entries.append(entry)
            self.entries_red.append(row_entries)

        # Center the Red Team table
        self.red_table_frame.pack(side=tk.TOP, pady=5)

        column1_label_green = tk.Label(self.green_table_frame, text="Unique ID", font=("Helvetica", 15), width=8, anchor="w", bg=self.GREEN, fg=self.WHITE)
        column1_label_green.grid(row=0, column=1, padx=(5, 0), pady=5)

        column2_label_green = tk.Label(self.green_table_frame, text="Codename", font=("Helvetica", 15), width=8, anchor="w", bg=self.GREEN, fg=self.WHITE)
        column2_label_green.grid(row=0, column=2, padx=(5, 0), pady=5)

        column3_label_green = tk.Label(self.green_table_frame, text="Equipment ID", font=("Helvetica", 15), width=11, anchor="w", bg=self.GREEN, fg=self.WHITE)
        column3_label_green.grid(row=0, column=3, padx=(5, 0), pady=5)

        # Create 15x3 tables with Entry widgets and row numbers for the Green Team
        self.entries_green = []
        for i in range(1, self.TEAM_SIZE + 1):
            row_label = tk.Label(self.green_table_frame, text=f"{i}.", font = ("Helvetica", 15), width=3, anchor="w", bg=self.GREEN, fg=self.WHITE)
            row_label.grid(row=i, column=0, padx=(5, 0), pady=5)

            row_entries = []
            for j in range(1, 4):
                entry = tk.Entry(self.green_table_frame, font=("Helvetica", 15), width=20, bg=self.WHITE, fg="black")
                entry.grid(row=i, column=j, padx=5, pady=3)
                entry.bind("<FocusOut>", lambda event, row=i, col=j, entry=entry: self.on_entry_change(event, row, col, entry, 'green'))
                row_entries.append(entry)
            self.entries_green.append(row_entries)

        # Center the Green Team table
        self.green_table_frame.pack(side=tk.TOP, pady=5)

    def on_button_click(self, button_number):
        if button_number == 5:
            self.start_game()
        elif button_number == 8:
            self.clear_entries()
            
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

        # If they've edited in the UniqueID column...
        if col == 1:
            # go get the player
            codename = self.controller.databaseManager.getPlayer(value)
            # if it's red team...
            if team == 'red':
                self.entries_red[row-1][col].delete(0, tk.END) # This clears the codename field before we insert the ID's codename so they dont stack
                # if a codename was retrieved from database
                if codename is not None:
                    # put string in entry field
                    self.entries_red[row-1][col].insert(0, codename)
            if team == 'green':
                self.entries_green[row-1][col].delete(0, tk.END)
                # if a codename was retrieved from database
                if codename is not None:
                    # put string in entry field
                    self.entries_green[row-1][col].insert(0, codename)
        # else if they're changing codename
        elif col == 2:
            # if it's red team
            if team == 'red':
                tempUniqueID = self.entries_red[row - 1][0].get()
            else:
                tempUniqueID = self.entries_green[row - 1][0].get()
            # retrieve player from database by id
            codename = self.controller.databaseManager.getPlayer(tempUniqueID)
            if codename is None:    # If the codename is none then this ID hasn't been registered yet, so we add them.
                self.controller.databaseManager.addPlayer(tempUniqueID, value)
            else:   # else, we update with the new name
                self.controller.databaseManager.updatePlayer(tempUniqueID, value)

    # go through tables and creates a list of Player objects for each team and sends it to renderingManager
    def export_players(self):
        red_team_out = []
        green_team_out = []
        can_submit = True

        for i in range(self.TEAM_SIZE):
            entry_unique_id = self.entries_red[i][0].get()
            entry_codename = self.entries_red[i][1].get()
            entry_equip_id = self.entries_red[i][2].get()

            # if there is a codename and an equipment id...
            if entry_codename != "" and entry_equip_id != "":
                # create a red Player
                red_team_out.append(Player(entry_codename, int(entry_equip_id), 'red'))
                # notify networkingManager that equip id is in use
                self.controller.networkingManager.send_broadcast(entry_equip_id)
            # otherwise, if the row is NOT COMPLETELY empty... (i.e. there might be an equip id but no codename)
            elif not (entry_codename == "" and entry_equip_id == "" and entry_unique_id == ""):
                # don't let user submit
                can_submit = False

            entry_unique_id = self.entries_green[i][0].get()
            entry_codename = self.entries_green[i][1].get()
            entry_equip_id = self.entries_green[i][2].get()

            # if there is a codename and an equipment id...
            if entry_codename != "" and entry_equip_id != "":
                # create a green Player
                green_team_out.append(Player(entry_codename, int(entry_equip_id), 'green'))
                # notify networkingManager that equip id is in use
                self.controller.networkingManager.send_broadcast(entry_equip_id)
            # otherwise, if the row is NOT COMPLETELY empty... (i.e. there might be an equip id but no codename)
            elif not (entry_codename == "" and entry_equip_id == "" and entry_unique_id == ""):
                # don't let user submit
                can_submit = False

        # if the user can submit (all player entries are fully filled out)
        if can_submit:
            # set the model's teams
            self.controller.set_model_teams(green_team_out, red_team_out)
        
        return can_submit

    # function to clear all entries
    def clear_entries(self):
        for i in range(self.TEAM_SIZE):
            for j in range(1, 4):
                # Clears the entry table
                self.entries_red[i][j-1].delete(0, tk.END)
                self.entries_green[i][j-1].delete(0, tk.END)

    # function to start game
    def start_game(self):
        can_start = self.export_players()
        if can_start:
            self.controller.start_game()
        else:
            self.build_error_popup()

    # Function to display the error popup
    def build_error_popup(self):
        self.popup_frame = tk.Frame(self, bg=self.WHITE, bd=5, relief=tk.SOLID, highlightbackground="yellow", highlightthickness=5)
        self.popup_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        error_msg = "There was an error filling out the teams. Please make sure all players have all entries filled."
        label = tk.Label(self.popup_frame, text=error_msg, bg=self.WHITE, fg=self.RED)
        label.pack(pady=20)

        btn_quit = tk.Button(self.popup_frame, text="Return to Player Entry", command=self.close_popup, bg=self.WHITE, fg=self.RED)
        btn_quit.pack(pady=10)

    def close_popup(self):
        if hasattr(self, "popup_frame") and self.popup_frame:
            self.popup_frame.destroy()

    def on_show(self):
        pass