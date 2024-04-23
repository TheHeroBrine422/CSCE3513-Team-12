from enum import Enum

class Stage(Enum):
        ENTER_TEAMS = 0
        STARTING = 1
        ACTIVE_GAME = 2
        FINISHED = 3
        PROGRAM_QUIT = 4