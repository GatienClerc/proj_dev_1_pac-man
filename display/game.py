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
    font = pygame.font.Font("assets/font/Pacfont-ZEBZ.ttf")
    return board, font
    

def game_screen(screen, board):
    display_wall(screen, board)
    draw_score(screen, font, score)

def display_wall(screen, board):
    for col in board:
        for tile in col:
            if isinstance(tile, Wall):
                tile.draw(screen)

def draw_score(screen, font, score):

    text = font.render(f"SCORE {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))