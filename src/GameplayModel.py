from Player import Player
from Stage import Stage

class GameplayModel():
    GREEN_TEAM_CODE = 43
    RED_TEAM_CODE  = 53
    red_team = [] # list of Player objects
    green_team = [] # list of Player objects
    gameplayScreen = None
    renderingManager = None
    networkingManager = None
    state = None

    def __init__(self):
        self.running = True
        self.state = Stage.ENTER_TEAMS
        self.red_team_score = 0
        self.green_team_score = 0

    def set_game_state(self, newState):
        self.state = newState
        print("state is: " + self.state.name)

    def set_renderer(self, rm):
        self.renderingManager = rm

    def set_networker(self, nm):
        self.networkingManager = nm

    def set_screen(self, gameplayScreen):
        self.gameplayScreen = gameplayScreen

    def set_teams(self, green_team_in, red_team_in):
        self.red_team = red_team_in
        self.green_team = green_team_in
        self.gameplayScreen.set_teams(self.red_team, self.green_team)

    def reset(self):
        self.set_game_state(Stage.ENTER_TEAMS)
        self.red_team.clear()
        self.green_team.clear()
        self.red_team_score = 0
        self.green_team_score = 0

    # To be used by networkingManager
    def shots_fired(self, fire_equip_id, hit_equip_id):
        firing_player = Player()
        hit_player = Player()

        # Find players with matching equipment ids
        for player in self.red_team:
            if (player.equipment_id == fire_equip_id):
                firing_player = player
            
            if (player.equipment_id == hit_equip_id):
                hit_player = player

        for player in self.green_team:
            if (player.equipment_id == fire_equip_id):
                firing_player = player
            
            if (player.equipment_id == hit_equip_id):
                hit_player = player

        # If they're on different teams, firing player gets 10 pts
        if (firing_player.team != hit_player.team):
            firing_player.score += 10
        # Otherwise firing player loses 10 pts
        else:
            firing_player.score -= 10

        self.gameplayScreen.add_hit(firing_player, hit_player)
        self.sort_teams()
        self.update_gameplay_screen()

    # To be used by networkingManager
    def base_hit(self, player_equip_id, base_id):
        firing_player = Player()
        # Find firing player
        for player in self.red_team:
            if (player.equipment_id == player_equip_id):
                firing_player = player

        for player in self.green_team:
            if (player.equipment_id == player_equip_id):
                firing_player = player

        # If the red base was hit AND the player is on the green team
        if ((base_id == self.RED_TEAM_CODE) and (firing_player.team == 'green')):
            # player gets 100 pts
            firing_player.score += 100
        # Otherwise if the green base was hit AND the player is on the red team
        elif ((base_id == self.GREEN_TEAM_CODE) and (firing_player.team == 'red')):
            # player gets 100 pts
            firing_player.score += 100

        # add message on screen
        self.gameplayScreen.add_base_hit(firing_player, base_id)
        # resort teams
        self.sort_teams()
        # update screen
        self.update_gameplay_screen()
            
    def get_team_scores(self):
        # create a list of tuples, each containing a team and their total score
        team_scores = [sum (player.score for player in self.red_team), 
                       sum (player.score for player in self.green_team)]
        
        return team_scores
    
    def sort_teams(self):
        # Sort the teams by player score
        self.red_team = sorted(self.red_team, key=lambda player: player.score, reverse=True) # list of Players
        self.green_team = sorted(self.green_team, key=lambda player: player.score, reverse=True) # list of Players

    def start_game(self):
        self.set_game_state(Stage.ACTIVE_GAME)
        self.networkingManager.send_broadcast("202")

    def end_game(self):
        self.set_game_state(Stage.FINISHED)
        self.networkingManager.send_broadcast("221")
        self.networkingManager.send_broadcast("221")
        self.networkingManager.send_broadcast("221")

    def update_gameplay_screen(self):
        # reformat the score
        self.gameplayScreen.format_score(self.get_team_scores())
        # redisplay teams in new order
        self.gameplayScreen.update_teams(self.red_team, self.green_team)