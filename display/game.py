import pygame

def game(screen):
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 40)

    running = True
    while running:
        screen.fill((0, 0, 100))

        text = font.render("Jeu en cours... Appuyez sur ESC pour le menu", True, (255, 255, 255))
        screen.blit(text, (50, 220))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "menu"

        pygame.display.flip()
        clock.tick(60)
