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

from classes.Ghost import Ghost
from utils.read_gamedata import read_gamedata
from utils.wall_tileset import set_wall_image

def game_innit(game_area, tile_size, pixel_size):
    board = read_gamedata(tile_size, game_area, pixel_size)
    set_wall_image(board, pixel_size)
    img = pygame.image.load("assets/sprites/ghost/ghost.png")
    ghost = Ghost(1, 5, pixel_size, tile_size, game_area, img)
    return board, ghost
    

def game_screen(screen, board, ghost):
    display_board(screen, board)
    display_ghost(screen, ghost, board)


def display_board(screen, board):
    for col in board:
        for tile in col:
            tile.draw(screen)

def display_ghost(screen, ghost, board):
    ghost.draw(screen)
    ghost.move(board)