import pygame
from display.game import game_innit, display_elements
#from utils.movement_manager import *
pygame.init()

PIXEL_SIZE = 3
TILE_SIZE = 8 * PIXEL_SIZE
WIDTH = 28 * TILE_SIZE
HEIGHT = 36 * TILE_SIZE

SCORE = 0 * TILE_SIZE
GAME = 3 * TILE_SIZE
FOOT = 34 * TILE_SIZE

clock = pygame.time.Clock()
running = True
screen = pygame.display.set_mode((WIDTH, HEIGHT))

board, player = game_innit(GAME, TILE_SIZE, PIXEL_SIZE)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()
    #player_movement(screen, board, pressed_keys, player, PIXEL_SIZE, TILE_SIZE, WIDTH, GAME, FOOT)

    pygame.display.flip()

    screen.fill((0, 0, 0))
    display_elements(screen, board, player)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
