import pygame

def setting(screen, width, height, font):

    clock = pygame.time.Clock()

    volume = 70
    pixel_size = 3
    dragging = False

    slider_x = width // 2 - 150
    slider_y = 180
    slider_width = 300

    btn_minus = pygame.Rect(width // 2 - 100, 300, 50, 50)
    btn_plus = pygame.Rect(width // 2 + 50, 300, 50, 50)
    btn_back = pygame.Rect(width // 2 - 100, 450, 200, 60)

    while True:

        screen.fill((0, 0, 0))

        # Titre
        title = font.render("SETTINGS", True, (255, 255, 255))
        screen.blit(title, title.get_rect(center=(width // 2, 80)))

        # Volume
        volume_text = font.render(f"Volume : {int(volume)}%", True, (255, 255, 255))
        screen.blit(volume_text, (slider_x, 130))

        pygame.draw.rect(
            screen,
            (255, 255, 255),
            (slider_x, slider_y, slider_width, 10)
        )

        handle_x = slider_x + (volume / 100) * slider_width

        pygame.draw.circle(
            screen,
            (255, 255, 0),
            (int(handle_x), slider_y + 5),
            12
        )

        # Pixel Size
        pixel_label = font.render("Pixel Size :", True, (255, 255, 255))
        screen.blit(pixel_label, (width // 2 - 120, 250))

        pygame.draw.rect(screen, (255, 255, 255), btn_minus)
        pygame.draw.rect(screen, (255, 255, 255), btn_plus)

        minus_text = font.render("<", True, (0, 0, 0))
        plus_text = font.render(">", True, (0, 0, 0))

        screen.blit(minus_text, minus_text.get_rect(center=btn_minus.center))
        screen.blit(plus_text, plus_text.get_rect(center=btn_plus.center))

        size_text = font.render(f"{pixel_size}x", True, (255, 255, 255))
        screen.blit(size_text, size_text.get_rect(center=(width // 2, 325)))

        # Back
        pygame.draw.rect(screen, (255, 255, 255), btn_back)

        back_text = font.render("BACK", True, (0, 0, 0))
        screen.blit(back_text, back_text.get_rect(center=btn_back.center))

        # Événements
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "menu"

            if event.type == pygame.MOUSEBUTTONDOWN:

                if btn_back.collidepoint(event.pos):
                    return "menu"

                if btn_minus.collidepoint(event.pos):
                    pixel_size = max(1, pixel_size - 1)

                if btn_plus.collidepoint(event.pos):
                    pixel_size = min(5, pixel_size + 1)

                if abs(event.pos[0] - handle_x) < 15:
                    dragging = True

            if event.type == pygame.MOUSEBUTTONUP:
                dragging = False

            if event.type == pygame.MOUSEMOTION and dragging:

                volume = (
                    (event.pos[0] - slider_x)
                    / slider_width
                ) * 100

                volume = max(0, min(100, volume))

                pygame.mixer.music.set_volume(volume / 100)

        pygame.display.flip()
        clock.tick(60)