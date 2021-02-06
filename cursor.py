import pygame
from pygame.sprite import Sprite

class Cursor(Sprite):
    """Una clase para cambiar el cursor del ratón"""
    def __init__(self):
        super().__init__()
        self.cursor_image = pygame.image.load('images/buttons/cursor.png')
        self.cursor_image_rect = self.cursor_image.get_rect()
