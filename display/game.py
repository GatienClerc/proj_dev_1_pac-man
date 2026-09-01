#***********************************************************************************************************************
# Program name:         game.py
# Description:          the game screen
# Author:               Cédric Jankiewicz
# Creation date:        23.08.2026
# Modified by:          Gatien Clerc
# Modification date:    01.09.26
# Version:              0.3
#***********************************************************************************************************************
import pygame
from classes.Wall import Wall
from utils.read_gamedata import read_gamedata
from utils.wall_tileset import set_wall_image

def game(screen):
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 40)

    running = True
    while running:
        screen.fill((0, 0, 100))

        text = font.render("Jeu en cours... Appuyez sur ESC pour le menu", True, (255, 255, 255))
        screen.blit(text, (50, 220))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "menu"

        pygame.display.flip()
        clock.tick(60)

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