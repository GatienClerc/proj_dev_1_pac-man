import pygame
from classes.Wall import Wall
from utils.spritesheet import spritesheet

def set_wall_image(board, pixel_size):
    """
    set_wall_image set the wall images depending of their neighbors
    :param board: the game board
    :param pixel_size: the size of 1 pixel
    """
    sprites = spritesheet("assets/sprites/terrain/wall.png", 4, 4, 8, 8)
    for i in range (len(board)):
        for j in range (len(board[i])):
            if isinstance(board[i][j], Wall) and not board[i][j].is_gate:
                neighbors = get_neighbors(board, i, j)
                image = ruleset.get(tuple(neighbors), [-1, 0])
                if image[0] != -1:
                    board[i][j].image = pygame.transform.rotate(sprites[image[0]], image[1])
                else:
                    board[i][j].image = pygame.Surface((0, 0), pygame.SRCALPHA)
            
            elif isinstance(board[i][j], Wall) and board[i][j].is_gate:
                board[i][j].image = pygame.image.load("assets/sprites/terrain/ghost_gate.png")


def get_neighbors(board, i, j):
    """
    get_neighbors get all the neighbors
    :param board: the game board
    :param i: x coordinate
    :param j: y coordinate
    :return: a set of neighbors
    """
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
                
            elif cell.is_ghost_area:
                neighbors.append(3)
                
            else:
                neighbors.append(0)

    return neighbors


def rotate_90(rule):
    """
    rotate_90 rotate a rule by 90 degrees
    :param rule: the rule to rotate
    :return: the rotated rule
    """
    return (
        rule[2],rule[4],rule[7],
        rule[1],        rule[6],
        rule[0],rule[3],rule[5],
    )


def add_rotations(rule, value):
    """
    add_rotations add the 4 rotation to the ruleset
    :param rule: the rule to rotate
    :param value: the image from the spritesheet
    """
    for i in range(4):
        ruleset[rule]=[value,90*i]
        rule = rotate_90(rule)
    

ruleset = {}

#corner
add_rotations(
    (
    0, 0, 0,
    0,    1,
    0, 1, 1
    ),0)

#inner corner
add_rotations(
    (
    1, 1, 1,
    1,    1,
    1, 1, 0
    ),0)

#wall
add_rotations(
    (
    0, 0, 0,
    1,    1,
    1, 1, 1
    ),1)

#wall corner L
add_rotations(
    (
    1, 0, 0,
    1,    1,
    1, 1, 1
    ),1)

# wall corner R
add_rotations(
    (
    0, 0, 1,
    1,    1,
    1, 1, 1
    ),1)

# wall dead end
add_rotations(
    (
    1, 0, 1,
    1,    1,
    1, 1, 1
    ),1)

#outside corner
add_rotations(
    (
    2, 2, 2,
    2,    1,
    2, 1, 0
    ),2)

#inner outside corner L
add_rotations(
    (
    2, 1, 1,
    2,    1,
    2, 1, 0
    ),4)

# inner outside corner R
add_rotations(
    (
    2, 2, 2,
    1,    1,
    1, 1, 0
    ),5)

#outside wall
add_rotations(
    (
    2, 2, 2,
    1,    1,
    0, 0, 0
    ),3)

#outside wall corner L
add_rotations(
    (
    2, 2, 2,
    1,    1,
    1, 0, 0
    ),3)

#outside wall corner R
add_rotations(
    (
    2, 2, 2,
    1,    1,
    0, 0, 1
    ),3)

#outside wall dead end
add_rotations(
    (
    2, 2, 2,
    1,    1,
    1, 0, 1
    ),3)

#outside wall volume
add_rotations(
    (
    1, 1, 1,
    1,    1,
    2, 2, 2
    ),12)

#exit corner L
add_rotations(
    (
    2, 1, 1,
    2,    1,
    2, 0, 0
    ),13)

#exit corner R
add_rotations(
    (
    1, 1, 2,
    1,    2,
    0, 0, 2
    ),14)

#ghost room corner
add_rotations(
    (
    0, 0, 0,
    0,    1,
    0, 1, 3
    ),6)

# ghost room wall
add_rotations(
    (
    0, 0, 0,
    1,    1,
    3, 3, 3
    ),7)

# ghost room corner wall L
add_rotations(
    (
    0, 0, 0,
    1,    1,
    1, 3, 3
    ),7)

# ghost room corner wall R
add_rotations(
    (
    0, 0, 0,
    1,    1,
    3, 3, 1
    ),7)

# ghost room end wall L
add_rotations(
    (
    0, 0, 0,
    1,    0,
    3, 3, 3
    ),8)

# ghost room end wall R
add_rotations(
    (
    0, 0, 0,
    0,    1,
    3, 3, 3
    ),9)