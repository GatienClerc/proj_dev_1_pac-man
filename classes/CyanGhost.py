#***********************************************************************************************************************
# Program name:         Ghost.py
# Description:          Class for Cyan Ghost
# Author:               Cédric Jankiewicz
# Creation date:        01.09.2026
# Modified by:          -
# Modification date:    -
# Version:              0.1
#***********************************************************************************************************************

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

#import
from classes.Ghost import Ghost


class CyanGhost(Ghost):
    def __init__(self, pos_x, pos_y, pixel_size=1, tile_size=8, game_area=24):
        super().__init__(pos_x, pos_y, pixel_size, tile_size, game_area, color=(0,255,255))
        self.red_ghost = None
        self.wait_time = 240
        self.scatter_target = [26, 29]
    
    def chase(self, player):
        dir = player.last_direction
        dx, dy = DIRECTIONS[dir]
        pivot = [player.grid_x+(2*dx), player.grid_y+(2*dy)]
        #get opposite of the pivot
        target_x = 2 * pivot[0] - self.red_ghost.grid_x
        target_y = 2 * pivot[1] - self.red_ghost.grid_y
        return [target_x, target_y]