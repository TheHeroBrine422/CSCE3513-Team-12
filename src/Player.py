class Player():
    def __init__(self, player_name = None, player_equipment_id = None, player_team = None):
        self.name = player_name
        self.equipment_id = player_equipment_id
        self.team = player_team
        self.score = 0