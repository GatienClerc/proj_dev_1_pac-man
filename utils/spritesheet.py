import pygame

def spritesheet(image_path, rows, cols, width, height, size=1):
    textures = []
    image = pygame.image.load(image_path)

    for j in range(rows):
        for i in range(cols):
            texture = image.subsurface(
                pygame.Rect(
                    width * i,
                    height * j,
                    width,
                    height
                )
            )
            texture = pygame.transform.scale_by(texture, size)
            textures.append(texture)

    return textures
