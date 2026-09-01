#***********************************************************************************************************************
# Program name:         Ghost.py
# Description:          Class for Red Ghost
# Author:               Cédric Jankiewicz
# Creation date:        01.09.2026
# Modified by:          -
# Modification date:    -
# Version:              0.1
#***********************************************************************************************************************

#import
from classes.Ghost import Ghost


class RedGhost(Ghost):
    def __init__(self, pos_x, pos_y, pixel_size=1, tile_size=8, game_area=24):
        super().__init__(pos_x, pos_y, pixel_size, tile_size, game_area, color=(255,0,0))