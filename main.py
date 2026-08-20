import pygame
from pygame.locals import *

pygame.init()


WIDTH = 672
HEIGHT = 864
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
