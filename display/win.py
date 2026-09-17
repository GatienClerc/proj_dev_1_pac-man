#***********************************************************************************************************************
# Program name:         win.py
# Description:          the win screen
# Author:               Gatien Clerc
# Creation date:        17.09.2026
# Modified by:          -
# Modification date:    -
# Version:              0.1
#***********************************************************************************************************************
import pygame

pygame.init()

def win(screen, width, height, font):
    clock = pygame.time.Clock()

    title_y = height // 8

    while True:
        screen.fill((0,0,0))

        title = font.render("YOU WIN !!!", True, (255, 255, 255))
        screen.blit(title, title.get_rect(center=(width // 2, title_y)))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "menu"

        pygame.display.flip()
        clock.tick(60)