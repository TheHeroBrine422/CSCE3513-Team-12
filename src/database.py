import os
from supabase import create_client

# Supabase connection
url = "https://saiciiruhdotdjxznipy.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNhaWNpaXJ1aGRvdGRqeHpuaXB5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDgwMjc4NzEsImV4cCI6MjAyMzYwMzg3MX0.QmYOxHO_M-10pN_eW_Gy4SOpbZ8F0DepmcVTxAzkmy8"

supabase = create_client(url, key)

class DatabaseManager():
    def __init__(self, gameState):
        self.gameState = gameState
        # add database connection stuff here

    # implement database functions for other portions of the code to use.
    
    
    # Testing whether the connection works
    response = supabase.table('countries').select("*").execute()
    print(response)

