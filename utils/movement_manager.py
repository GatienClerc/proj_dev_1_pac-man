#***********************************************************************************************************************
# Program name:         movement_manager.py
# Description:          Utilitary that will manage player and enemy movements
# Author:               Thierry Perroud
# Creation date:        27.08.2026
# Modified by:          -
# Modification date:    -
# Version:              0.1
#***********************************************************************************************************************
########################################################################################################################
# Imports                                                                                                              #
########################################################################################################################
import pygame

########################################################################################################################
# Functions                                                                                                            #
########################################################################################################################
def player_movement(screen, board, pressed_keys, player, one_pixel, one_tile, max_x, min_y, max_y):
    direction = None

    # Determines in which direction the player will attempt to move
    if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]: direction = "up"
    elif pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]: direction = "left"
    elif pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN]: direction = "down"
    elif pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]: direction = "right"
    elif player.direction: direction = player.direction
    elif player.buffered_direction: direction = player.buffered_direction

    # If the player is already moving in a direction, then there won't be any wall when going back
    if player.direction == "up" and direction == "down" or player.direction == "down" and direction == "up" or player.direction == "left" and direction == "right" or player.direction == "right" and direction == "up":
        player.direction = direction

    # If there is a wall in the way, then the direction is buffered for when there won't be a wall in the way
    elif is_wall_in_the_way(board, direction, player, one_pixel):
        player.buffered_direction = direction

    # If the player is centered and there's no wall, then the player can change direction
    elif check_for_centered_player():
        player.direction = direction

    player.move(screen, one_pixel, one_tile, max_x, min_y, max_y)


def is_wall_in_the_way(board, direction, player, one_pixel):
    # TODO: check if there is a wall in the way of the player

    for col in board:
        for tile in col:
            pass

    return False

def check_for_centered_player():
    # TODO: check if the player is centered on the tile
    return True