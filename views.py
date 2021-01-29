import pygame

class Views():
    """Una clase para administrar las vistas"""
    def __init__(self):
        """Inicia los valores para las vistas"""
        #Fondos
        self.fondo_intro = pygame.image.load("images/fondo_intro.png")
        self.fondo_prueba = pygame.image.load("images/fondo_prueba.png")
