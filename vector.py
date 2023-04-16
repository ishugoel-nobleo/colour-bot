import random
import numpy as np
from ..bot_control import Move

class Vector:
    # Declare global variable
    # direction = 1 # 0=stay, 1=up, 2=right, 3=down, 4=left

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
        # Chooses a random target location, and moves there.
        # Once it's there, choose a new location.
        x = self.position[0]
        y = self.position[1]
        l = grid.shape[0] # always square
                
        if self.direction == 1:
            if y < (l - 1) and self.can_overwrite(self.id, grid[y+1][x]):
                return Move.UP
            elif x < (l - 1):
                self.direction = 2
                return Move.RIGHT
            elif x > 0:
                self.direction = 4
                return Move.LEFT
            else:                   # can be removed
                self.direction = 3
                return Move.DOWN
        
        if self.direction == 2:
            if x < (l - 1) and self.can_overwrite(self.id, grid[y][x+1]):
                return Move.RIGHT
            elif y < (l - 1):
                self.direction = 1
                return Move.UP
            elif y > 0:
                self.direction = 3
                return Move.DOWN
            else:
                self.direction = 4
                return Move.LEFT

        if self.direction == 3:
            if y > 0 and self.can_overwrite(self.id, grid[y-1][x]):
                return Move.DOWN
            elif x > 0:
                self.direction = 4
                return Move.LEFT
            elif x < (l - 1):
                self.direction = 2
                return Move.RIGHT
            else:
                self.direction = 1
                return Move.UP

        if self.direction == 4:
            if x > 0 and self.can_overwrite(self.id, grid[y][x - 1]):
                return Move.LEFT
            elif y > 0:
                self.direction = 3
                return Move.DOWN
            elif y < (l - 1):
                self.direction = 1
                return Move.UP            
            else:
                self.direction = 2
                return Move.RIGHT
        
        return Move.STAY
        
        # # Create a target in storage if doesn't exist
        # if  self.target is None:
        #     self.target = np.zeros_like(self.position)

        # # If reached the target find a new target
        # if np.array_equal(self.position, self.target):
        #     self.target[0] = random.randint(0, grid.shape[0] - 1)
        #     self.target[1] = random.randint(0, grid.shape[1] - 1)
        
        # # Move in direction of target
        # if self.target[0] > self.position[0]:
        #     return Move.RIGHT
        # elif self.target[0] < self.position[0]:
        #     return Move.LEFT
        # elif self.target[1] > self.position[1]:
        #     return Move.UP
        # else:
        #     return Move.DOWN