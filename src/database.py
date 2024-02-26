import os
from supabase import create_client


class DatabaseManager():
    def __init__(self, gameState):
        self.gameState = gameState
        url = "https://saiciiruhdotdjxznipy.supabase.co"
        key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNhaWNpaXJ1aGRvdGRqeHpuaXB5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDgwMjc4NzEsImV4cCI6MjAyMzYwMzg3MX0.QmYOxHO_M-10pN_eW_Gy4SOpbZ8F0DepmcVTxAzkmy8"

        # Supabase connection
        self.supabase = create_client(url, key)

    def getUsers(self):
        # Testing whether the connection works
        response = self.supabase.table('Players').select("*").execute()
        return response.data

    def getPlayer(self, id):
        existing_player, error = self.supabase.table('Players').select('*').eq('id', id).execute()
        if error and not (error[0] == 'count' and error[1] is None):
            print(f"Error: {error}")
            return None
        if existing_player:
            return existing_player[0]['codename']
        else:
            print("Player not found")
            return None
    
    def addPlayer(self, id, codename):
        # Check to see if the player already exists
        existing_player, error = self.supabase.table('Players').select('*').eq('id', id).execute()
        if error and not (error[0] == 'count' and error[1] is None):
            print(f"Error: {error}")
        elif len(existing_player[1]) > 0:
            print(f"Player already exists: {existing_player}")
        else:
            data, error2 = self.supabase.table('Players').insert([{'id': id, 'codename': codename}]).execute()
            if error2:
                print(f"Error: {error}")
            else:
                print(f"Player {id} - {codename} added successfully")
                
    def clearTable(self):
        data, error = self.supabase.table('Players').delete().execute()
        if error:
            print(f"Error: {error}")
        else:
            print(f"Table cleared successfully")
        

    
if __name__ == "__main__":
    databaseManager = DatabaseManager({})
    databaseManager.getUsers()

