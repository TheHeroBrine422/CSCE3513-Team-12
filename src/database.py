from supabase import create_client


class DatabaseManager():
    def __init__(self):
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
        if not (error[0] == 'count' and error[1] is None):
            print(f"Error: {error}")
            return None
        if len(existing_player[1]) > 0:
            return existing_player[1][0]['codename']
        else:
            print("Player not found")
            return None
    
    def updatePlayer(self, player_id, new_codename):
        try:
            existing_player, error = self.supabase.table('Players').select('*').eq('id', player_id).execute()
            if not (error[0] == 'count' and error[1] is None):
                print(f"Error: {error}")
            elif existing_player[1]:
                # Player found, update the codename
                _, update_error = self.supabase.table('Players').update({'codename': new_codename}).eq('id', player_id).execute()
                if not (update_error[0] == 'count' and update_error[1] is None):
                    print(f"Error updating player: {update_error}")
                else:
                    print(f"Player {player_id} - Codename updated to {new_codename}")
            else:
                print("Player not found")
        except Exception as e:
            print(f"Error: {e}")
    
    def addPlayer(self, id, codename):
        # Check to see if the player already exists
        existing_player, error = self.supabase.table('Players').select('*').eq('id', id).execute()
        if not (error[0] == 'count' and error[1] is None):
            print(f"Error: {error}")
        elif len(existing_player[1]) > 0:
            print(f"Player already exists: {existing_player}")
        else:
            data, error2 = self.supabase.table('Players').insert([{'id': id, 'codename': codename}]).execute()
            if not (error2[0] == 'count' and error2[1] is None):
                print(f"Error: {error}")
            else:
                print(f"Player {id} - {codename} added successfully")
                
    def clearTable(self):
        data, error = self.supabase.table('Players').delete().execute()
        if not (error[0] == 'count' and error[1] is None):
            print(f"Error: {error}")
        else:
            print(f"Table cleared successfully")