# ***********************************************************************************************************************
# Program name:         game.py
# Description:          the game screen
# Author:               Cédric Jankiewicz
# Creation date:        23.08.2026
# Modified by:          -
# Modification date:    -
# Version:              0.1
# ***********************************************************************************************************************
from classes.Wall import Wall
from utils.read_gamedata import read_gamedata


def game_innit(game_area, tile_size, pixel_size):
    board, player = read_gamedata(tile_size, game_area, pixel_size)
    return board, player


def display_elements(screen, board, player):
    display_wall(screen, board)
    display_player(screen, player)


def display_wall(screen, board):
    for col in board:
        for tile in col:
            if isinstance(tile, Wall):
                tile.draw(screen)

def display_player(screen, player):
    player.draw(screen)