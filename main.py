import pygame
from pygame.locals import *

pygame.init()

TILE_SIZE = 24
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

    clock.tick(60)
    screen.fill((0,0,0))
    pygame.display.flip()

pygame.quit()
