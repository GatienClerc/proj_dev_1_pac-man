import pygame
from display.game import game_screen

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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    screen.fill((0,0,0))
    game_screen(screen, GAME, TILE_SIZE, PIXEL_SIZE)
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()
