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

from classes.Player import Player

from classes.RedGhost import RedGhost
from classes.CyanGhost import CyanGhost
from classes.PinkGhost import PinkGhost
from classes.OrangeGhost import OrangeGhost

def read_gamedata(tile_size, game_area, pixel_size):
    """
    read_gamedata reads the game data from a txt file
    :param tile_size: the size of a tile 
    :param game_area: the game area coordinate
    :param pixel_size: the size of a pixel
    :return: the gameboard
    """
    file_path = "gamedata/board.txt"
    board = []
    player = None
    ghosts = []

    with open(file_path, "r") as f:
        count_row = 0
        for line in f:
            row = []
            count_col = 0
            for char in line.rstrip("\n"):
                if char == "*":
                    row.append(Wall(tile_size * count_col, game_area + tile_size * count_row, pixel_size))
                
                elif char == "-":
                    row.append(Wall(tile_size * count_col, game_area + tile_size * count_row, pixel_size, is_gate=True))
                    
                elif char == "%":
                    row.append(Ground(tile_size * count_col, game_area + tile_size * count_row, pixel_size, is_ghost_area=True))
                    
                elif char == "#":
                    row.append(Ground(tile_size * count_col, game_area + tile_size * count_row, pixel_size, item_type="Power Up"))
                    
                elif char == ".":
                    row.append(Ground(tile_size * count_col, game_area + tile_size * count_row, pixel_size, item_type="Dot"))

                elif char == "P":
                    player = Player(count_col, count_row, pixel_size, tile_size, game_area)
                    row.append(Ground(tile_size * count_col,
                                      game_area + tile_size * count_row,
                                      pixel_size))
                
                elif char == "r":
                    ghosts.append(RedGhost(count_col, count_row, pixel_size, tile_size, game_area))
                    row.append(Ground(tile_size * count_col,
                                      game_area + tile_size * count_row,
                                      pixel_size))
                
                elif char == "c":
                    ghosts.append(CyanGhost(count_col, count_row, pixel_size, tile_size, game_area))
                    row.append(Ground(tile_size * count_col,
                                      game_area + tile_size * count_row,
                                      pixel_size, is_ghost_area=True))
                
                elif char == "p":
                    ghosts.append(PinkGhost(count_col, count_row, pixel_size, tile_size, game_area))
                    row.append(Ground(tile_size * count_col,
                                      game_area + tile_size * count_row,
                                      pixel_size, is_ghost_area=True))
                
                elif char == "o":
                    ghosts.append(OrangeGhost(count_col, count_row, pixel_size, tile_size, game_area))
                    row.append(Ground(tile_size * count_col,
                                      game_area + tile_size * count_row,
                                      pixel_size, is_ghost_area=True))
                
                else:
                    row.append(Ground(tile_size*count_col, game_area+tile_size*count_row, pixel_size))
                    
                count_col += 1
            board.append(row)
            count_row += 1
    
    for ghost in ghosts:
        if isinstance(ghost, CyanGhost):
            for g in ghosts:
                if isinstance(g, RedGhost):
                    ghost.red_ghost = g
    
    return board, player, ghosts