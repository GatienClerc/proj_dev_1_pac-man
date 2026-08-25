import pygame
from classes.Wall import Wall
from utils.spritesheet import spritesheet

def set_wall_image(board, pixel_size):
    sprites = spritesheet("assets/sprites/terrain/wall.png", 3, 4, 8, 8, pixel_size)
    for i in range (len(board)):
        for j in range (len(board[i])):
            if isinstance(board[i][j], Wall):
                neighbors = get_neighbors(board, i, j)
                image = ruleset.get(tuple(neighbors), [-1, 0])
                if image[0] != -1:
                    board[i][j].image = pygame.transform.rotate(sprites[image[0]], image[1])
                else:
                    board[i][j].image = pygame.Surface((0, 0), pygame.SRCALPHA)

def get_neighbors(board, i, j):
    directions = [
        (-1, -1),  # top-left
        (-1,  0),  # top
        (-1,  1),  # top-right
        ( 0, -1),  # left
        ( 0,  1),  # right
        ( 1, -1),  # bottom-left
        ( 1,  0),  # bottom
        ( 1,  1),  # bottom-right
    ]

    neighbors = []

    for di, dj in directions:
        ni = i + di
        nj = j + dj

        # Outside the board = void
        if ni < 0 or ni >= len(board) or nj < 0 or nj >= len(board[ni]):
            neighbors.append(2)
        else:
            cell = board[ni][nj]

            if isinstance(cell, Wall):
                neighbors.append(1)
            else:
                neighbors.append(0)

    return neighbors

ruleset = {
    #corner
    (0,0,0,
     0,  1,
     0,1,1) : [0, 0],
    (0,1,1,
     0,  1,
     0,0,0) : [0, 90],
    (1,1,0,
     1,  0,
     0,0,0): [0, 180],
    (0,0,0,
     1,  0,
     1,1,0): [0, 270],
}