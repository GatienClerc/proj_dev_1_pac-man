import pygame
from read_gamedata import read_gamedata

def display_board(coordinates, tile_size, screen):
    board = read_gamedata("gamedata/board.txt")
    print(board)
    wall = pygame.image.load("assets/sprites/terrain/wall.png")
    wall = pygame.transform.scale(wall, (tile_size, tile_size))
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '*':
                print("yes")
                screen.blit(wall, (coordinates[0]+tile_size*j, coordinates[1]+tile_size*i))
                