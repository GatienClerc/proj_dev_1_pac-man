#***********************************************************************************************************************
# Program name:         Ghost.py
# Description:          Class for Pink Ghost
# Author:               Cédric Jankiewicz
# Creation date:        01.09.2026
# Modified by:          -
# Modification date:    -
# Version:              0.1
#***********************************************************************************************************************

#import
from classes.Ghost import Ghost

# Directions:
# 0 = South
# 1 = East
# 2 = North
# 3 = West
DIRECTIONS = (
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
)

class PinkGhost(Ghost):
    def __init__(self, pos_x, pos_y, pixel_size=1, tile_size=8, game_area=24):
        super().__init__(pos_x, pos_y, pixel_size, tile_size, game_area, color=(255,184,255))
        self.wait_time = 480
        self.scatter_target = [1, 1]
    
    def chase(self, player):
        dir = player.last_direction
        dx, dy = DIRECTIONS[dir]
        return [player.grid_x+(4*dx), player.grid_y+(4*dy)]