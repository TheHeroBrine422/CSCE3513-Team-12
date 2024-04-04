from networking import NetworkingManager
from render import RenderingManager
from database import DatabaseManager
from GameplayModel import GameplayModel

gameplayModel = GameplayModel()

databaseManager = DatabaseManager()
databaseManager.getUsers()
networkingManager = NetworkingManager(gameplayModel)
gameplayModel.set_networker(networkingManager)
renderingManager = RenderingManager(gameplayModel, networkingManager, databaseManager)
gameplayModel.set_renderer(renderingManager)

while gameplayModel.running:
    networkingManager.tick()
    renderingManager.tick()