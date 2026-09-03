import pygame

pygame.init()

def menu(screen, width, height, font):
    clock = pygame.time.Clock()

    btn_width = width // 3
    btn_height = height // 12

    btn_x = (width - btn_width) // 2

    spacing = height // 8

    btn_play = pygame.Rect(btn_x, height // 2 - spacing, btn_width, btn_height)
    btn_setting = pygame.Rect(btn_x, height // 2, btn_width, btn_height)
    btn_quit = pygame.Rect(btn_x, height // 2 + spacing, btn_width, btn_height)

    running = True
    while running:
        screen.fill((0,0,0))

        pygame.draw.rect(screen, (255, 255, 255), btn_play)
        text_play = font.render("Play", True, (0, 0, 0))
        screen.blit(text_play, text_play.get_rect(center=btn_play.center))

        pygame.draw.rect(screen, (255, 255, 255), btn_setting)
        text_setting = font.render("Setting", True, (0, 0, 0))
        screen.blit(text_setting, text_setting.get_rect(center=btn_setting.center))

        pygame.draw.rect(screen, (255, 255, 255), btn_quit)
        text_quit = font.render("Quit", True, (0, 0, 0))
        screen.blit(text_quit, text_quit.get_rect(center=btn_quit.center))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_play.collidepoint(event.pos):
                    return "game"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_setting.collidepoint(event.pos):
                    return "setting"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_quit.collidepoint(event.pos):
                    return "quit"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "quit"

        pygame.display.flip()
        clock.tick(60)