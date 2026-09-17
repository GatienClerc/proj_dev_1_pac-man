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

def win(screen, width, height, font, score):
    clock = pygame.time.Clock()

    btn_y = height // 8
    btn_width = width // 3
    btn_height = height // 12
    btn_x = (width - btn_width) // 2
    spacing = height // 8

    btn_menu = pygame.Rect(btn_x, height // 2 + spacing, btn_width, btn_height)

    while True:
        screen.fill((0,0,0))

        title = font.render("YOU WIN !!!", True, (255, 255, 255))
        title = pygame.transform.scale_by(title, 2)
        screen.blit(title, title.get_rect(center=(width // 2, btn_y)))

        score_txt = font.render(f"{score}", True, ('white'))
        screen.blit(score_txt, score_txt.get_rect(center=(width // 2, btn_y + btn_x )))

        pygame.draw.rect(screen, (255, 255, 255), btn_menu)
        text_quit = font.render("Menu", True, (0, 0, 0))
        screen.blit(text_quit, text_quit.get_rect(center=btn_menu.center))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "menu"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_menu.collidepoint(event.pos):
                    return "menu"

        pygame.display.flip()
        clock.tick(60)