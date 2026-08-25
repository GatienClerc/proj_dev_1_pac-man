import pygame
from classes.Wall import Wall
from utils.spritesheet import spritesheet

def set_wall_image(board, pixel_size):
    sprites = spritesheet("assets/sprites/terrain/wall.png", 4, 4, 8, 8, pixel_size)
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
    (0, 0, 0,
     0,    1,
     0, 1, 1) : [0, 0],
    (0, 1, 1,
     0,    1,
     0, 0, 0) : [0, 90],
    (1, 1, 0,
     1,    0,
     0, 0, 0): [0, 180],
    (0, 0, 0,
     1,    0,
     1, 1, 0): [0, 270],
    #inner corner
    (1, 1, 1,
     1,    1,
     1, 1, 0): [0, 0],
    (1, 1, 0,
     1,    1,
     1, 1, 1): [0, 90],
    (0, 1, 1,
     1,    1,
     1, 1, 1): [0, 180],
    (1, 1, 1,
     1,    1,
     0, 1, 1): [0, 270],
    #wall
    (0, 0, 0,
     1,    1,
     1, 1, 1): [1, 0],
    (0, 1, 1,
     0,    1,
     0, 1, 1) : [1, 90],
    (1, 1, 1,
     1,    1,
     0, 0, 0): [1, 180],
    (1, 1, 0,
     1,    0,
     1, 1, 0): [1, 270],
    #wall corner L
    (1, 0, 0,
     1,    1,
     1, 1, 1): [1, 0],
    (0, 1, 1,
     0,    1,
     1, 1, 1): [1, 90],
    (1, 1, 1,
     1,    1,
     0, 0, 1): [1, 180],
    (1, 1, 1,
     1,    0,
     1, 1, 0): [1, 270],
    # wall corner R
    (0, 0, 1,
     1,    1,
     1, 1, 1): [1, 0],
    (1, 1, 1,
     0,    1,
     0, 1, 1): [1, 90],
    (1, 1, 1,
     1,    1,
     1, 0, 0): [1, 180],
    (1, 1, 0,
     1,    0,
     1, 1, 1): [1, 270],
    # wall exit L
    (0, 0, 2,
     1,    2,
     1, 1, 2): [1, 0],
    (2, 2, 2,
     0,    1,
     0, 1, 1) : [1, 90],
    (2, 1, 1,
     2,    1,
     2, 0, 0): [1, 180],
    (1, 1, 0,
     1,    0,
     2, 2, 2): [1, 270],
    # wall exit R
    (2, 0, 0,
     2,    1,
     2, 1, 1): [1, 0],
    (0, 1, 1,
     0,    1,
     2, 2, 2): [1, 90],
    (1, 1, 2,
     1,    2,
     0, 0, 2): [1, 180],
    (2, 2, 2,
     1,    0,
     1, 1, 0): [1, 270],
    #outside corner
    (2, 2, 2,
     2,    1,
     2, 1, 0): [2, 0],
    (2, 1, 0,
     2,    1,
     2, 2, 2): [2, 90],
    (0, 1, 2,
     1,    2,
     2, 2, 2): [2, 180],
    (2, 2, 2,
     1,    2,
     0, 1, 2): [2, 270],
    #inner outside corner L
    (2, 1, 1,
     2,    1,
     2, 1, 0): [4, 0],
    (1, 1, 0,
     1,    1,
     2, 2, 2): [4, 90],
    (0, 1, 2,
     1,    2,
     1, 1, 2): [4, 180],
    (2, 2, 2,
     1,    1,
     0, 1, 1): [4, 270],
    # inner outside corner R
    (2, 2, 2,
     1, 1,
     1, 1, 0): [5, 0],
    (2, 1, 0,
     2,    1,
     2, 1, 1): [5, 90],
    (0, 1, 1,
     1,    1,
     2, 2, 2): [5, 180],
    (1, 1, 2,
     1,    2,
     0, 1, 2): [5, 270],
    #outside wall
    (2, 2, 2,
     1,    1,
     0, 0, 0): [3, 0],
    (2, 1, 0,
     2,    0,
     2, 1, 0): [3, 90],
    (0, 0, 0,
     1,    1,
     2, 2, 2): [3, 180],
    (0, 1, 2,
     0,    2,
     0, 1, 2): [3, 270],
    #outside wall corner L
    (2, 2, 2,
     1,    1,
     1, 0, 0): [3, 0],
    (2, 1, 1,
     2,    0,
     2, 1, 0): [3, 90],
    (0, 0, 1,
     1,    1,
     2, 2, 2): [3, 180],
    (1, 1, 2,
     0,    2,
     0, 1, 2): [3, 270],
    #outside wall corner R
    (2, 2, 2,
     1,    1,
     0, 0, 1): [3, 0],
    (2, 1, 0,
     2,    0,
     2, 1, 1): [3, 90],
    (1, 0, 0,
     1,    1,
     2, 2, 2): [3, 180],
    (0, 1, 2,
     0,    2,
     1, 1, 2): [3, 270],
    #outside wall volume
    (2, 2, 2,
     1,    1,
     1, 1, 1): [12, 180],
    (2, 1, 1,
     2,    1,
     2, 1, 1): [12, 270],
    (1, 1, 1,
     1,    1,
     2, 2, 2): [12, 0],
    (1, 1, 2,
     1,    2,
     1, 1, 2): [12, 90],
    #exit corner L
    (2, 1, 1,
     2,    1,
     2, 0, 0): [13, 0],
    (1, 1, 0,
     1,    0,
     2, 2, 2): [13, 90],
    (0, 0, 2,
     1,    2,
     1, 1, 2): [13, 180],
    (2, 2, 2,
     0,    1,
     0, 1, 1): [13, 270],
    # exit corner R
    (1, 1, 2,
     1,    2,
     0, 0, 2): [14, 0],
    (2, 2, 2,
     1,    0,
     1, 1, 0): [14, 90],
    (2, 0, 0,
     2,    1,
     2, 1, 1): [14, 180],
    (0, 1, 1,
     0,    1,
     2, 2, 2): [14, 270],
}