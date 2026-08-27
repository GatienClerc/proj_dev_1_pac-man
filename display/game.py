#***********************************************************************************************************************
# Program name:         game.py
# Description:          the game screen
# Author:               Cédric Jankiewicz
# Creation date:        23.08.2026
# Modified by:          -
# Modification date:    -
# Version:              0.1
#***********************************************************************************************************************
import pygame
from classes.Wall import Wall
from utils.read_gamedata import read_gamedata
from utils.wall_tileset import set_wall_image


def game_innit(game_area, tile_size, pixel_size):
    board = read_gamedata(tile_size, game_area, pixel_size)
    set_wall_image(board, pixel_size)
    return board
    

def game_screen(screen, board, font ,score, tile_size):
    display_wall(screen, board)
    draw_score(screen, font, score, tile_size)

def display_wall(screen, board):
    for col in board:
        for tile in col:
            if isinstance(tile, Wall):
                tile.draw(screen)

def draw_score(screen, font, score, tile_size):
    text_1up = font.render(f"1UP", True, ('white'))
    screen.blit(text_1up, (tile_size * 3, 0))

    text_2up = font.render(f"HIGH SCORE", True, ('white'))
    screen.blit(text_2up, (tile_size * 9, 0))

    text = font.render(f"{score}", True, ('white'))
    screen.blit(text, (tile_size * 5, tile_size))