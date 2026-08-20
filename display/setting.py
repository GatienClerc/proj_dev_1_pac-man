import pygame

def setting(screen):
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 40)

    running = True
    while running:
        screen.fill((0, 0, 0))

        text = font.render("Setting", True, (255, 255, 255))
        screen.blit(text, (50, 220))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "menu"

        pygame.display.flip()
        clock.tick(60)
