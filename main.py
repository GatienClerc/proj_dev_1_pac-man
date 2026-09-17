#***********************************************************************************************************************
# Program name:         main.py
# Description:          the main programme
# Author:               Gatien Clerc
# Creation date:        08.09.2026
# Modified by:          -
# Modification date:    -
# Version:              0.3
#***********************************************************************************************************************
import pygame
from display.menu import menu
from display.setting import setting
from display.game import game_innit, game_screen, reset_entities
from utils.save import load

pygame.init()
settings = load()

volume = settings["audio"]
PIXEL_SIZE = settings["pixel_size"]

TILE_SIZE = 8 * PIXEL_SIZE
WIDTH = 28 * TILE_SIZE
HEIGHT = 36 * TILE_SIZE

SCORE = 0 * TILE_SIZE
GAME = 3 * TILE_SIZE
FOOT = 34 * TILE_SIZE

pygame.display.set_caption("Pac-Man")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font("assets/font/Pacfont.ttf", TILE_SIZE)

state = menu(screen, WIDTH, HEIGHT, font)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

board, player, ghosts = game_innit(GAME, TILE_SIZE, PIXEL_SIZE)

while state != "quit":
    if state == "menu":
        state = menu(screen, WIDTH, HEIGHT, font)

    elif state == "setting":
        state, PIXEL_SIZE, volume = setting(screen, WIDTH, HEIGHT, font, PIXEL_SIZE, volume)

        TILE_SIZE = 8 * PIXEL_SIZE

        WIDTH = 28 * TILE_SIZE
        HEIGHT = 36 * TILE_SIZE

        SCORE = 0 * TILE_SIZE
        GAME = 3 * TILE_SIZE
        FOOT = 34 * TILE_SIZE

        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        font = pygame.font.Font("assets/font/Pacfont.ttf",TILE_SIZE)

    elif state == "game":
        board, player, ghosts = game_innit(GAME, TILE_SIZE,PIXEL_SIZE)

        running_game = True

        while running_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    state = "quit"
                    running_game = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        state = "menu"
                        running_game = False
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        player.buffered_direction = 2
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        player.buffered_direction = 1
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        player.buffered_direction = 0
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        player.buffered_direction = 3

            

            screen.fill((0, 0, 0))
            game_screen(screen, board, font, TILE_SIZE, player, ghosts)
            pygame.display.flip()
        
            if not player.is_alive: reset_entities(player, ghosts)
            
            clock.tick(60)
pygame.quit()
