from tkinter import font

import pygame
from display.game import game_screen, game_innit

pygame.init()

PIXEL_SIZE = 3
TILE_SIZE = 8*PIXEL_SIZE
WIDTH = 28*TILE_SIZE
HEIGHT = 36*TILE_SIZE

SCORE = 0*TILE_SIZE
GAME = 3*TILE_SIZE
FOOT = 34*TILE_SIZE

clock = pygame.time.Clock()
running = True
screen = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.Font("assets/font/Pacfont.ttf", TILE_SIZE)

board = game_innit(GAME, TILE_SIZE, PIXEL_SIZE)

score = "00"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    screen.fill((0,0,0))
    game_screen(screen, board, font, score, TILE_SIZE)
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()
