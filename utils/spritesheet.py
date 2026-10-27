import pygame

def spritesheet(image_path, rows, cols, width, height):
    """
    spritesheet cut a image into a list of smaller images
    :param image_path: the image path
    :param rows: number of rows
    :param cols: number of columns 
    :param width: the width of one image
    :param height: the height of one image
    :return: a list of images 
    """
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
            textures.append(texture)

    return textures
