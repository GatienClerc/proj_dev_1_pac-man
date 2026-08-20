import pygame
from display.elements.display_wall import display_board

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

    screen.fill((0,0,0))
    pygame.draw.line(screen, (255,255,255), (0,GAME), (WIDTH, GAME))
    display_board([0, GAME], TILE_SIZE, screen)
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()
