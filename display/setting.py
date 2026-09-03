import pygame

def setting(screen, width, height, font, pixel_size, volume):

    clock = pygame.time.Clock()

    volume = 70
    dragging = False

    title_y = height // 8

    slider_width = width // 2
    slider_x = (width - slider_width) // 2
    slider_y = height // 4

    btn_size = height // 12

    btn_minus = pygame.Rect(width // 2 - btn_size * 2, height // 2, btn_size, btn_size)

    btn_plus = pygame.Rect( width // 2 + btn_size, height // 2, btn_size, btn_size)

    btn_apply_width = width // 3
    btn_apply_height = height // 12

    btn_apply = pygame.Rect((width - btn_apply_width) // 2, height * 3 // 4, btn_apply_width, btn_apply_height)

    while True:

        screen.fill((0, 0, 0))

        # Titre
        title = font.render("SETTINGS", True, (255, 255, 255))
        screen.blit(title, title.get_rect(center=(width // 2, title_y)))

        # Volume
        volume_text = font.render(f"Volume : {int(volume)}%", True, (255, 255, 255))
        screen.blit(volume_text, (slider_x, slider_y - btn_size))


        pygame.draw.rect(screen,(255, 255, 255),(slider_x, slider_y, slider_width, btn_size // 5))

        handle_x = slider_x + (volume / 100) * slider_width

        pygame.draw.circle( screen,(255, 255, 0),(int(handle_x), slider_y + btn_size // 10),btn_size // 4)

        # Pixel Size
        pixel_label = font.render("Pixel Size :", True, (255, 255, 255))
        screen.blit(pixel_label,(width // 2 - pixel_label.get_width() // 2, height // 2 - btn_size))

        pygame.draw.rect(screen, (255, 255, 255), btn_minus)
        pygame.draw.rect(screen, (255, 255, 255), btn_plus)

        minus_text = font.render("<", True, (0, 0, 0))
        plus_text = font.render(">", True, (0, 0, 0))

        screen.blit(minus_text, minus_text.get_rect(center=btn_minus.center))
        screen.blit(plus_text, plus_text.get_rect(center=btn_plus.center))

        size_text = font.render(f"{pixel_size}x", True, (255, 255, 255))
        screen.blit(size_text, size_text.get_rect(center=(width // 2, height // 2 + btn_size // 2)))

        # apply
        pygame.draw.rect(screen, (255, 255, 255), btn_apply)

        apply_text = font.render("APPLY", True, (0, 0, 0))
        screen.blit(apply_text, apply_text.get_rect(center=btn_apply.center))

        # Événements
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "menu", pixel_size

            if event.type == pygame.MOUSEBUTTONDOWN:

                if btn_apply.collidepoint(event.pos):
                    return "menu", pixel_size

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