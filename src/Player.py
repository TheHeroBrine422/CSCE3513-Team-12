class Player():
    def __init__(self, player_name = "N/A", player_equipment_id = -1, player_team = "N/A", player_score = 0, player_got_base_hit = False):
        self.name = player_name
        self.equipment_id = player_equipment_id
        self.team = player_team
        self.score = player_score
        self.got_base_hit = player_got_base_hit

    def toString(self):
        return ("name: " + self.name + " equip_id: " + str(self.equipment_id) + " team: " + self.team)