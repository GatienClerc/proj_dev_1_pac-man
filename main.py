import pygame
from display.menu import menu
from display.game import game
from display.setting import setting


pygame.init()
width = 672
height = 864

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pac-Man")
etat = menu(screen, width)

etat = "menu"
while etat != "quit":
    if etat == "menu":
        etat = menu(screen, width)
    elif etat == "game":
        etat = game(screen)

    elif etat == "setting":
        etat = setting(screen)

pygame.quit()
