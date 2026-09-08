#***********************************************************************************************************************
# Program name:         game.py
# Description:          the game screen
# Author:               Cédric Jankiewicz
# Creation date:        23.08.2026
# Modified by:          -
# Modification date:    -
# Version:              0.1
#***********************************************************************************************************************
from utils.read_gamedata import read_gamedata
from utils.wall_tileset import set_wall_image

global_ghosts_state = "scatter"
global_ghosts_timer = 0

def game_innit(game_area, tile_size, pixel_size):
    board, player, ghosts = read_gamedata(tile_size, game_area, pixel_size)
    set_wall_image(board, pixel_size)
    return board, player, ghosts


def game_screen(screen, board, player, ghosts):
    display_board(screen, board)
    display_player(screen, player, board)
    display_ghosts(screen, ghosts, board, player)
    update_ghosts(ghosts)


def display_board(screen, board):
    for col in board:
        for tile in col:
            tile.draw(screen)


def display_player(screen, player, board):
    player.move(board)
    player.draw(screen)


def display_ghosts(screen, ghosts, board, player):  
    for ghost in ghosts:
        ghost.draw(screen)
        ghost.move(board, player)


def update_ghosts(ghosts):
    global global_ghosts_state, global_ghosts_timer
    global_ghosts_timer += 1
    
    if global_ghosts_state == "scatter" and global_ghosts_timer > 7*60:
        global_ghosts_state = "chase"
        global_ghosts_timer = 0
        
    elif global_ghosts_state == "chase" and global_ghosts_timer > 20*60:
        global_ghosts_state = "scatter"
        global_ghosts_timer = 0
    
    for ghost in ghosts:
        ghost.change_state_to(global_ghosts_state)