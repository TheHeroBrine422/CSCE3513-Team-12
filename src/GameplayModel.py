from Player import Player

class GameplayModel():
    GREEN_TEAM_CODE = 43
    RED_TEAM_CODE  = 53
    red_team = [] # list of Player objects
    green_team = [] # list of Player objects
    screen = None

    def __init__(self):
        self.red_team_score = 0
        self.green_team_score = 0

    def set_screen(self, gameplayScreen):
        self.screen = gameplayScreen

    def set_teams(self, green_team_in, red_team_in):
        self.red_team = red_team_in
        self.green_team = green_team_in
        self.screen.set_teams(self.red_team, self.green_team)

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
            if (firing_player.team == 'green'):
                self.green_team_score += 10
            else:
                self.red_team_score += 10
        # Otherwise firing player loses 10 pts
        else:
            firing_player.score -= 10
            if (firing_player.team == 'green'):
                self.green_team_score -= 10
            else:
                self.red_team_score -= 10

    # To be used by networkingManager
    def base_hit(self, base_id, player_equip_id):
        # Find firing player
        for player in self.red_team:
            if (player.equipment_id == player_equip_id):
                firing_player = player

        for player in self.green_team:
            if (player.equipment_id == player_equip_id):
                firing_player = player

        # If the red base was hit AND the player is on the green team
        if ((base_id == self.RED_TEAM_CODE) and (firing_player.team == 'green')):
            # green team gets 100 pts
            self.green_team_score += 100
        # Otherwise if the green base was hit AND the player is on the red team
        elif ((base_id == self.GREEN_TEAM_CODE) and (firing_player.team == 'red')):
            # red team gets 100 pts
            self.red_team_score += 100