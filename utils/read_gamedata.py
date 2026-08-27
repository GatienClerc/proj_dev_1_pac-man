#***********************************************************************************************************************
# Program name:         read_gamedata.py
# Description:          read the board data and instantiate the tile object
# Author:               Cédric Jankiewicz
# Creation date:        23.08.2026
# Modified by:          -
# Modification date:    -
# Version:              0.1
#***********************************************************************************************************************
from classes.Ground import Ground
from classes.Wall import Wall

def read_gamedata(tile_size, game_area, pixel_size):
    file_path = "gamedata/board.txt"
    board = []

    with open(file_path, "r") as f:
        count_row = 0
        for line in f:
            row = []
            count_col = 0
            for char in line.rstrip("\n"):
                if char == "*":
                    row.append(Wall(tile_size*count_col, game_area+tile_size*count_row, pixel_size))
                elif char == "%":
                    row.append(Ground(tile_size * count_col, game_area + tile_size * count_row, pixel_size, is_ghost_area=True))
                else:
                    #TODO check all posibilities
                    row.append(Ground(tile_size*count_col, game_area+tile_size*count_row, pixel_size))
                count_col += 1
            board.append(row)
            count_row += 1

    return board