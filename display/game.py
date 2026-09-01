#***********************************************************************************************************************
# Program name:         game.py
# Description:          the game screen
# Author:               Cédric Jankiewicz
# Creation date:        23.08.2026
# Modified by:          -
# Modification date:    -
# Version:              0.1
#***********************************************************************************************************************
import pygame.image

from classes.RedGhost import RedGhost
from classes.CyanGhost import CyanGhost
from classes.PinkGhost import PinkGhost
from classes.OrangeGhost import OrangeGhost
from utils.read_gamedata import read_gamedata
from utils.wall_tileset import set_wall_image

def game_innit(game_area, tile_size, pixel_size):
    board = read_gamedata(tile_size, game_area, pixel_size)
    set_wall_image(board, pixel_size)
    ghosts = [
        RedGhost(13.5, 11, pixel_size, tile_size, game_area),
        CyanGhost(11.5, 14, pixel_size, tile_size, game_area),
        PinkGhost(13.5, 14, pixel_size, tile_size, game_area),
        OrangeGhost(15.5, 14, pixel_size, tile_size, game_area)
    ]
    return board, ghosts
    

def game_screen(screen, board, ghosts):
    display_board(screen, board)
    display_ghosts(screen, ghosts, board)


def display_board(screen, board):
    for col in board:
        for tile in col:
            tile.draw(screen)

def display_ghosts(screen, ghosts, board):
    for ghost in ghosts:
        ghost.draw(screen)
        ghost.move(board)