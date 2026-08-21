import pygame
from classes.Wall import Wall

from read_gamedata import read_gamedata

def game_screen(screen, game_area, tile_size):
    board = read_gamedata(tile_size, game_area)
    display_wall(screen, board)

def display_wall(screen, board):
    for col in board:
        for tile in col:
            if isinstance(tile, Wall):
                tile.draw(screen)