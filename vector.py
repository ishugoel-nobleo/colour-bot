import random
import numpy as np
from ..bot_control import Move

class Vector:

    def __init__(self):
        self.direction = 1 # 0=stay, 1=up, 2=right, 3=down, 4=left
        
    def get_name(self):
        return "Vector"

    def get_contributor(self):
        return "Ishu"

    def can_overwrite(self, id, tile):
        if tile == 0: return True
        return (id - tile) % 3 == 2

    def determine_next_move(self, grid, enemies, game_info):
        # logic
        x = self.position[0]
        y = self.position[1]
        l = grid.shape[0] # always square
                
        if self.direction == 1:
            if y < (l - 1) and self.can_overwrite(self.id, grid[y+1][x]):
                return Move.UP
            elif x < (l - 1):
                self.direction = 2
                return Move.RIGHT
            else:
                self.direction = 4
                return Move.LEFT
        
        if self.direction == 2:
            if x < (l - 1) and self.can_overwrite(self.id, grid[y][x+1]):
                return Move.RIGHT
            elif y < (l - 1):
                self.direction = 1
                return Move.UP
            else:
                self.direction = 3
                return Move.DOWN

        if self.direction == 3:
            if y > 0 and self.can_overwrite(self.id, grid[y-1][x]):
                return Move.DOWN
            elif x > 0:
                self.direction = 4
                return Move.LEFT
            else:
                self.direction = 2
                return Move.RIGHT

        if self.direction == 4:
            if x > 0 and self.can_overwrite(self.id, grid[y][x - 1]):
                return Move.LEFT
            elif y > 0:
                self.direction = 3
                return Move.DOWN
            else:
                self.direction = 1
                return Move.UP
        
        return Move.STAY
