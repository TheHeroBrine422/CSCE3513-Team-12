import tkinter as tk

class EntryScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#222222")

        # Create a header label
        header_label = tk.Label(self, text="Edit Current Game", font=("Helvetica", 16))
        header_label.pack(side=tk.TOP, pady=10)

        # Create 8 buttons
        buttons_frame = tk.Frame(self, bg="#222222")
        buttons_frame.pack(side=tk.BOTTOM, pady=10)

        buttons = []
        for i in range(1, 9):
            button = tk.Button(buttons_frame, text=f"Button {i}", command=lambda i=i: self.on_button_click(i))
            button.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)
            buttons.append(button)

        # Create frames for the Red and Green Teams, encapsulate them in another frame
        teams_frame = tk.Frame(self, bg="#222222")
        teams_frame.pack(side=tk.TOP)

        red_team_frame = tk.Frame(teams_frame, bd=2, relief=tk.GROOVE, bg="red")
        red_team_frame.pack(side=tk.LEFT, padx=10, pady=5, anchor="n")

        green_team_frame = tk.Frame(teams_frame, bd=2, relief=tk.GROOVE, bg="green")
        green_team_frame.pack(side=tk.LEFT, padx=10, pady=5, anchor="n")

        # Create labels for the Red and Green Teams
        red_team_label = tk.Label(red_team_frame, text="Red Team", font=("Helvetica", 14), bg="red")
        red_team_label.pack()

        green_team_label = tk.Label(green_team_frame, text="Green Team", font=("Helvetica", 14), bg="green")
        green_team_label.pack()

        # Create frames for the tables of the Red and Green Teams
        red_table_frame = tk.Frame(red_team_frame, bg="red")
        red_table_frame.pack()

        green_table_frame = tk.Frame(green_team_frame, bg="green")
        green_table_frame.pack()

        # Create 15x2 tables with Entry widgets and row numbers for the Red Team
        entries_red = []
        for i in range(15):
            row_label = tk.Label(red_table_frame, text=f"{i + 1}.", width=3, anchor="w", bg="red")
            row_label.grid(row=i, column=0, padx=(5, 0), pady=5)

            row_entries = []
            for j in range(1, 3):
                entry = tk.Entry(red_table_frame, width=20)
                entry.grid(row=i, column=j, padx=5, pady=5)
                entry.bind("<FocusOut>", lambda event, row=i, col=j, entry=entry: self.on_entry_change(event, row, col, entry))
                row_entries.append(entry)
            entries_red.append(row_entries)

        # Center the Red Team table
        red_table_frame.pack(side=tk.TOP, pady=5)

        # Create 15x2 tables with Entry widgets and row numbers for the Green Team
        entries_green = []
        for i in range(15):
            row_label = tk.Label(green_table_frame, text=f"{i + 1}.", width=3, anchor="w", bg="green")
            row_label.grid(row=i, column=0, padx=(5, 0), pady=5)

            row_entries = []
            for j in range(1, 3):
                entry = tk.Entry(green_table_frame, width=20)
                entry.grid(row=i, column=j, padx=5, pady=5)
                entry.bind("<FocusOut>", lambda event, row=i, col=j, entry=entry: self.on_entry_change(event, row, col, entry))
                row_entries.append(entry)
            entries_green.append(row_entries)

        # Center the Green Team table
        green_table_frame.pack(side=tk.TOP, pady=5)

    def on_button_click(self, button_number):
        print(f"Button {button_number} clicked!")

    # Function to handle changes in the Entry widgets
    def on_entry_change(self, event, row, col, entry):
        value = entry.get()
        print(f"Value in row {row}, column {col} changed to: {value}")