#***********************************************************************************************************************
# Program name:         game.py
# Description:          the game screen
# Author:               Cédric Jankiewicz
# Creation date:        23.08.2026
# Modified by:          -
# Modification date:    -
# Version:              0.1
#***********************************************************************************************************************
from classes.Wall import Wall
from utils.read_gamedata import read_gamedata
from utils.wall_tileset import set_wall_image

def game_innit(game_area, tile_size, pixel_size):
    board = read_gamedata(tile_size, game_area, pixel_size)
    set_wall_image(board, pixel_size)
    return board
    

def game_screen(screen, board):
    display_board(screen, board)

def display_board(screen, board):
    for col in board:
        for tile in col:
            tile.draw(screen)