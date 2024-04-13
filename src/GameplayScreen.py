import tkinter as tk
import random
import pygame
import os
from tkinter.font import Font
from Player import Player
from Stage import Stage

class GameplayScreen(tk.Frame):
    # Hex codes for colors
    PURPLE = '#4f62c4'
    RED = '#450c19'
    GREEN = '#093b15'
    GRAY = "#222222"
    WHITE = "#d9d9d9"
    HIT_STREAM_MAX = 5
    GREEN_TEAM_CODE = 43
    RED_TEAM_CODE  = 53
    STARTUP_LENGTH = 30
    GAME_LENGTH = 360

    def __init__(self, parent, controller, model):
        tk.Frame.__init__(self, parent, bg='black')
        pygame.mixer.init()
        self.controller = controller
        self.model = model
        self.red_team = [] # list of Player objects
        self.green_team = [] # list of Player objects
        self.hit_stream_texts = [] # list of Texts to display messages
        self.red_rows = [] # list of lists of Labels
        self.green_rows = [] # list of lists of Labels

        self.HEADER_FONT = Font(self.controller, family='Helvetica', size=48, weight='bold')
        self.PLAYER_FONT = Font(self.controller, family='Helvetica', size=24, weight='bold')
        self.SCORE_FONT = Font(self.controller, family='Helvetica', size=24)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=1)

        # Create frame for player SCORES on TOP of screen
        score_frame = tk.Frame(self, bg='black')
        score_frame.grid(row=0, column=0, sticky='nsew')
        score_frame.grid_rowconfigure(0, weight=1)
        score_frame.grid_rowconfigure(1, weight=5)
        score_frame.grid_columnconfigure(0, weight=1)
        score_frame.grid_columnconfigure(1, weight=1)
        score_frame.grid_columnconfigure(2, weight=1)
        score_frame.grid_columnconfigure(3, weight=1)

        # Create labels for the Red and Green Teams
        red_team_label = tk.Label(score_frame, text="RED TEAM", font=self.HEADER_FONT, bg=self.WHITE, fg=self.RED)
        red_team_label.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

        self.red_team_score_label = tk.Label(score_frame, text="0", font=self.HEADER_FONT, bg=self.WHITE, fg=self.RED)
        self.red_team_score_label.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')

        green_team_label = tk.Label(score_frame, text="GREEN TEAM", font=self.HEADER_FONT, bg=self.WHITE, fg=self.GREEN)
        green_team_label.grid(row=0, column=2, padx=5, pady=5, sticky='nsew')

        self.green_team_score_label = tk.Label(score_frame, text="0", font=self.HEADER_FONT, bg=self.WHITE, fg=self.GREEN)
        self.green_team_score_label.grid(row=0, column=3, padx=5, pady=5, sticky='nsew')

        # Create frame for each team
        self.red_team_frame = tk.Frame(score_frame, bd=2, relief=tk.GROOVE, bg=self.WHITE)
        self.red_team_frame.grid(row=1, column=0, padx=5, pady=5, columnspan=2, sticky='nsew')

        self.green_team_frame = tk.Frame(score_frame, bd=2, relief=tk.GROOVE, bg=self.WHITE)
        self.green_team_frame.grid(row=1, column=2, padx=5, pady=5, columnspan=2, sticky='nsew')

        # Create frames for the tables of the Red and Green Teams
        self.red_table_frame = tk.Frame(self.red_team_frame, bg=self.WHITE)
        self.red_table_frame.pack(side='left', padx=10, pady=5, anchor='w', fill='both', expand=True)
        self.red_table_frame.grid_columnconfigure(0, weight=1)
        self.red_table_frame.grid_columnconfigure(1, weight=3)
        self.red_table_frame.grid_columnconfigure(2, weight=1)

        self.green_table_frame = tk.Frame(self.green_team_frame, bg=self.WHITE)
        self.green_table_frame.pack(side='left', padx=10, pady=5, anchor='w', fill='both', expand=True)
        self.green_table_frame.grid_columnconfigure(0, weight=1)
        self.green_table_frame.grid_columnconfigure(1, weight=3)
        self.green_table_frame.grid_columnconfigure(2, weight=1)

        # Create frame for HIT STREAM in MIDDLE of screen
        self.hit_stream_frame = tk.Frame(self, bg=self.WHITE,padx=50)
        self.hit_stream_frame.grid(row=1, column=0, sticky='nsew')
        self.hit_stream_frame.grid_columnconfigure(0, weight=1)

        # Create frame for TIMER beneath HIT STREAM
        self.timer_frame = tk.Frame(self, bg=self.GRAY)
        self.timer_frame.grid(row=2, column=0, sticky='sew')

        # create timer label, but don't start the timer yet
        self.timer_label = tk.Label(self.timer_frame, text="6:00", font=self.HEADER_FONT, bg=self.GRAY, fg=self.WHITE)
        self.timer_label.pack()

    def on_show(self):
        # Start the countdown timer when the screen is shown
        self.remaining_time = self.STARTUP_LENGTH   # starting timer
        self.update_timer()  # Start the countdown

    # add a hit message to hit stream
    def add_hit(self, fired, hit):
        message = fired.name + " hit " + hit.name
        hit_text = tk.Text(self.hit_stream_frame, bg=self.WHITE, fg=self.GRAY, font=self.PLAYER_FONT, width=1, height=1, highlightthickness=0)
        hit_text.insert(tk.INSERT, message)
        hit_text.tag_add('p1', '1.0', '1.0 wordend')
        hit_text.tag_add('p2', 'end -2 chars wordstart', tk.END)
        if fired.team == 'red':
            hit_text.tag_config('p1', foreground=self.RED)
            hit_text.tag_config('p2', foreground=self.GREEN)
        else:
            hit_text.tag_config('p1', foreground=self.GREEN)
            hit_text.tag_config('p2', foreground=self.RED)
        hit_text.configure(state=tk.DISABLED)
        self.hit_stream_texts.append(hit_text)
        if (len(self.hit_stream_texts) > self.HIT_STREAM_MAX):
            self.hit_stream_texts.pop(0)
        self.format_hit_stream()

    def add_base_hit(self, fired, hit):
        base_name = ""
        if (hit == self.RED_TEAM_CODE):
            base_name = "RED BASE"
        else:
            base_name = "GREEN BASE"
        message = fired.name + " hit the " + base_name
        hit_text = tk.Text(self.hit_stream_frame, bg=self.WHITE, fg=self.GRAY, font=self.PLAYER_FONT, width=1, height=1, highlightthickness=0)
        hit_text.insert(tk.INSERT, message)
        hit_text.tag_add('p1', '1.0', '1.0 wordend')
        hit_text.tag_add('base', 'end -2 chars wordstart', tk.END)
        if fired.team == 'red':
            hit_text.tag_config('p1', foreground=self.RED)
            hit_text.tag_config('base', foreground=self.GREEN)
        else:
            hit_text.tag_config('p1', foreground=self.GREEN)
            hit_text.tag_config('base', foreground=self.RED)
        hit_text.configure(state=tk.DISABLED)
        self.hit_stream_texts.append(hit_text)
        if (len(self.hit_stream_texts) > self.HIT_STREAM_MAX):
            self.hit_stream_texts.pop(0)
        self.format_hit_stream()

    # reformat hit stream
    def format_hit_stream(self):
        # for each text
        for i in range(self.HIT_STREAM_MAX):
            # if we haven't run out of messages to display
            if (i < len(self.hit_stream_texts)):
                # display the message
                self.hit_stream_texts[i].grid(row=i, column=0, padx=(5, 0), pady=5, sticky='new')

    def set_teams(self, red, green):
        # Sort the teams by player score
        self.red_team = red # list of Players
        self.green_team = green # list of Players

        # Add player names + scores, sorted by score
        for i in range(0, len(self.red_team)):
            b_label = tk.Label(self.red_table_frame, text=u'\u24B7', anchor='w', bg=self.WHITE, fg=self.WHITE, font=self.PLAYER_FONT)
            b_label.grid(row=i, column=0, padx=(5, 0), pady=5, sticky='w')

            player_name = tk.Label(self.red_table_frame, text=self.red_team[i].name, anchor='w', bg=self.WHITE, fg=self.RED, font=self.PLAYER_FONT)
            player_name.grid(row=i, column=1, padx=(5, 0), pady=5, sticky='w')

            player_score = tk.Label(self.red_table_frame, text=self.red_team[i].score, anchor='e', bg=self.WHITE, fg=self.RED, font=self.SCORE_FONT)
            player_score.grid(row=i, column=2, padx=(5, 0), pady=5, sticky='e')

            self.red_rows.append([b_label, player_name, player_score])
        
        # Center the Red Team table
        self.red_table_frame.pack(side=tk.TOP, pady=5, fill='both', expand=True)

        for i in range(0, len(self.green_team)):
            b_label = tk.Label(self.green_table_frame, text=u'\u24B7', anchor='w', bg=self.WHITE, fg=self.WHITE, font=self.PLAYER_FONT)
            b_label.grid(row=i, column=0, padx=(5, 0), pady=5, sticky='w')

            player_name = tk.Label(self.green_table_frame, text=self.green_team[i].name, anchor='w', bg=self.WHITE, fg=self.GREEN, font=self.PLAYER_FONT)
            player_name.grid(row=i, column=1, padx=(5, 0), pady=5, sticky='w')

            player_score = tk.Label(self.green_table_frame, text=self.green_team[i].score, anchor='e', bg=self.WHITE, fg=self.GREEN, font=self.SCORE_FONT)
            player_score.grid(row=i, column=2, padx=(5, 0), pady=5, sticky='e')

            self.green_rows.append([b_label, player_name, player_score])
        
        # Center the Green Team table
        self.green_table_frame.pack(side=tk.TOP, pady=5, fill='both', expand=True)

    def update_teams(self, red, green):
        # Set the teams to what is being passed in (it's sorted by player score)
        self.red_team = red # list of Players
        self.green_team = green # list of Players

        # Update player names + scores, sorted by score
        for i in range(0, len(self.red_team)):
            if (self.red_team[i].got_base_hit):
                self.red_rows[i][0].config(fg=self.RED)
            self.red_rows[i][1].config(text = self.red_team[i].name)
            self.red_rows[i][2].config(text = self.red_team[i].score)

        for i in range(0, len(self.green_team)):
            if (self.green_team[i].got_base_hit):
                self.green_rows[i][0].config(fg=self.GREEN)
            self.green_rows[i][1].config(text = self.green_team[i].name)
            self.green_rows[i][2].config(text = self.green_team[i].score)

    def format_score(self, scores):
        # set red score label text
        self.red_team_score_label.config(text=str(scores[0]))
        # set green score label text
        self.green_team_score_label.config(text=str(scores[1]))

    # Countdown timer update function
    def update_timer(self):
        # get number of minutes
        minutes = self.remaining_time // 60
        # get number of seconds
        seconds = self.remaining_time % 60
        # set label text
        self.timer_label.config(text=f"{minutes:02}:{seconds:02}")
        # if we still have more time (i.e. more than 0 seconds left)
        if self.remaining_time > 0:
            # decrement
            self.remaining_time -= 1
            if self.model.state == Stage.STARTING and self.remaining_time == 16:
                self.play_photon_track()
            # update after a second
            self.after(1000, self.update_timer)
        # otherwise say game over
        elif self.model.state == Stage.STARTING:
            self.model.start_game()
            self.remaining_time = self.GAME_LENGTH
            self.update_timer()
        else:
            self.model.end_game()
            self.game_over_popup()

    # Function to display the "Game Over" popup
    def game_over_popup(self):
        self.popup_frame = tk.Frame(self, bg=self.WHITE, bd=5, relief=tk.SOLID, highlightbackground="yellow", highlightthickness=5)
        self.popup_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        label = tk.Label(self.popup_frame, text="Game Over!", font=self.HEADER_FONT, bg=self.WHITE, fg=self.RED)
        label.pack(pady=20)

        btn_quit = tk.Button(self.popup_frame, text="Quit", command=self.quit_to_entry_screen, font=self.SCORE_FONT, bg=self.RED, fg=self.WHITE)
        btn_quit.pack(pady=10)
    
    def quit_to_entry_screen(self):
        if hasattr(self, "popup_frame") and self.popup_frame:
            self.popup_frame.destroy()
        # Clear player names and scores
        self.clear_teams()
        self.model.reset()
        # Call the show_frame method of the controller (RenderingManager) to switch to the entry screen
        self.controller.show_frame("EntryScreen")

    def clear_teams(self):
        # Clear player names and scores from both teams
        self.red_team = []
        self.green_team = []
        # Destroy all labels displaying player names and scores
        for label_list in self.red_rows:
            for label in label_list:
                label.destroy()
        for label_list in self.green_rows:
            for label in label_list:
                label.destroy()
        # Clear the lists holding the labels
        self.red_rows = []
        self.green_rows = []
    
    def play_photon_track(self):
        PHOTON_TRACKS_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'photon_tracks'))
        # List available tracks
        tracks = [track for track in os.listdir(PHOTON_TRACKS_FOLDER) if os.path.isfile(os.path.join(PHOTON_TRACKS_FOLDER, track))]
        # Select a random track
        random.shuffle(tracks)
        track_name = tracks[0]
        # Construct the path to the selected track
        track_path = os.path.join(PHOTON_TRACKS_FOLDER, track_name)
        # Load and play the track
        print(f"Playing track: {track_name}")
        pygame.mixer.music.load(track_path)
        pygame.mixer.music.play()
