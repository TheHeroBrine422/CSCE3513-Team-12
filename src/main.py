from networking import NetworkingManager
from render import RenderingManager
from database import DatabaseManager
from GameplayModel import GameplayModel

gameState = {"running": True, "stage": "starting"} # global stuff like what players on what team, what is the current state of the game (starting, inprogress, finished) and other stuff like that.
gameplayModel = GameplayModel()

databaseManager = DatabaseManager(gameState)
networkingManager = NetworkingManager(gameState, gameplayModel)
renderingManager = RenderingManager(gameState, gameplayModel, networkingManager, databaseManager)

while gameState["running"]:
    networkingManager.tick()
    renderingManager.tick()