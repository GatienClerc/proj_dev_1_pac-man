import pygame

def spritesheet(image_path, row, col, width, height, size = 1):
    textures = []
    image = pygame.image.load(image_path)
    for i in range(col):
        for j in range(row):
            texture = image.subsurface(
                pygame.Rect(width*i, height*j, width, height)
            )
            texture = pygame.transform.scale_by(texture, size)
            textures.append(texture)
    return textures