import tkinter as tk

class EntryScreen(tk.Frame):
    def __init__(self, parent, controller):

        # Hex codes for colors
        PURPLE = '#4f62c4'
        RED = '#450c19'
        GREEN = '#093b15'
        GRAY = "#222222"
        WHITE = "#d9d9d9"

        tk.Frame.__init__(self, parent, bg=GRAY)

        # Create a header label
        header_label = tk.Label(self, text="Edit Current Game", font=("Helvetica", 20, "bold"), fg = PURPLE, bg=GRAY)
        header_label.pack(side=tk.TOP, pady=10)

        # Create 8 buttons
        buttons_frame = tk.Frame(self, bg=GRAY)
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
        teams_frame = tk.Frame(self, bg=GRAY)
        teams_frame.pack(side=tk.TOP)

        red_team_frame = tk.Frame(teams_frame, bd=2, relief=tk.GROOVE, bg=RED)
        red_team_frame.pack(side=tk.LEFT, padx=10, pady=5, anchor="n")

        green_team_frame = tk.Frame(teams_frame, bd=2, relief=tk.GROOVE, bg=GREEN)
        green_team_frame.pack(side=tk.LEFT, padx=10, pady=5, anchor="n")

        # Create labels for the Red and Green Teams
        red_team_label = tk.Label(red_team_frame, text="RED TEAM", font=("Helvetica", 16), bg=RED, fg=WHITE)
        red_team_label.pack()

        green_team_label = tk.Label(green_team_frame, text="GREEN TEAM", font=("Helvetica", 16), bg=GREEN, fg=WHITE)
        green_team_label.pack()

        # Create frames for the tables of the Red and Green Teams
        red_table_frame = tk.Frame(red_team_frame, bg=RED)
        red_table_frame.pack()

        green_table_frame = tk.Frame(green_team_frame, bg=GREEN)
        green_table_frame.pack()

        # Create 15x2 tables with Entry widgets and row numbers for the Red Team
        entries_red = []
        for i in range(15):
            row_label = tk.Label(red_table_frame, text=f"{i + 1}.", width=3, anchor="w", bg=RED, fg=WHITE)
            row_label.grid(row=i, column=0, padx=(5, 0), pady=5)

            row_entries = []
            for j in range(1, 3):
                entry = tk.Entry(red_table_frame, width=20, bg=WHITE, fg="black")
                entry.grid(row=i, column=j, padx=5, pady=5)
                entry.bind("<FocusOut>", lambda event, row=i, col=j, entry=entry: self.on_entry_change(event, row, col, entry))
                row_entries.append(entry)
            entries_red.append(row_entries)

        # Center the Red Team table
        red_table_frame.pack(side=tk.TOP, pady=5)

        # Create 15x2 tables with Entry widgets and row numbers for the Green Team
        entries_green = []
        for i in range(15):
            row_label = tk.Label(green_table_frame, text=f"{i + 1}.", width=3, anchor="w", bg=GREEN, fg=WHITE)
            row_label.grid(row=i, column=0, padx=(5, 0), pady=5)

            row_entries = []
            for j in range(1, 3):
                entry = tk.Entry(green_table_frame, width=20, bg=WHITE, fg="black")
                entry.grid(row=i, column=j, padx=5, pady=5)
                entry.bind("<FocusOut>", lambda event, row=i, col=j, entry=entry: self.on_entry_change(event, row, col, entry))
                row_entries.append(entry)
            entries_green.append(row_entries)

        # Center the Green Team table
        green_table_frame.pack(side=tk.TOP, pady=5)

    def on_button_click(self, button_number):
        print(f"Button {button_number} clicked!")

    def on_key_press(self, event):
        # Check if the pressed key is a function key (F1, F2, ..., F8)
        if event.keysym.startswith("F") and event.keysym[1:].isdigit():
            button_number = int(event.keysym[1:])
            self.on_button_click(button_number)

    # Function to handle changes in the Entry widgets
    def on_entry_change(self, event, row, col, entry):
        value = entry.get().strip()
        print(f"Value in row {row}, column {col} changed to: {value}")
