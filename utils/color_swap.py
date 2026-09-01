import pygame

def color_swap(image, old_c, new_c):
    """
    swap 2 colors in an images
    :param image: the image
    :param old_c: color to replace
    :param new_c: color to replace with
    :return: the new image
    """
    result = image.copy()
    pixels = pygame.PixelArray(result)

    pixels.replace(old_c, new_c)

    del pixels
    return result