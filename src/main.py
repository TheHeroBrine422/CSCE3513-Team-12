from networking import NetworkingManager
from render import RenderingManager
from database import DatabaseManager

gameState = {"running": True, "stage": "init"} # global stuff like what players on what team, what is the current state of the game (starting, inprogress, finished) and other stuff like that.

databaseManager = DatabaseManager(gameState)
networkingManager = NetworkingManager(gameState)
renderingManager = RenderingManager(gameState, networkingManager, databaseManager)

while gameState["running"]:
    networkingManager.tick()
    renderingManager.tick()