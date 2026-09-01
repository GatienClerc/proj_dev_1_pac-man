import pygame
from display.menu import menu
from display.setting import setting
from display.game import game_screen, game_innit, game

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
pygame.display.set_caption("Pac-Man")
etat = menu(screen, WIDTH)

etat = "menu"

while etat != "quit":
    if etat == "menu":
        etat = menu(screen, WIDTH)
    elif etat == "game":
        board = game_innit(GAME, TILE_SIZE, PIXEL_SIZE)
        etat = game(screen, board)
    elif etat == "setting":
        etat = setting(screen)
pygame.quit()

board = game_innit(GAME, TILE_SIZE, PIXEL_SIZE)