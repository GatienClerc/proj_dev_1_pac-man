import pygame
from display.game import game_innit, display_elements
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
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.buffered_direction = 2
            elif event.key == pygame.K_RIGHT:
                player.buffered_direction = 1
            elif event.key == pygame.K_DOWN:
                player.buffered_direction = 0
            elif event.key == pygame.K_LEFT:
                player.buffered_direction = 3

    pygame.display.flip()

    screen.fill((0, 0, 0))
    display_elements(screen, board, player)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
