import pygame

class Settings:
    """ Una clase para almacenar la configuración de celdaTP """

    def __init__(self):
        """ Inicializa la configuración del juego """

        # Configuración de pantalla
        self.screen_width = 960
        self.screen_height = 540
        self.fondo_intro = pygame.image.load("images/intro.png")
        self.screen = pygame.display.set_mode((self.screen_width,
                                              self.screen_height))
        self.icono = pygame.image.load("images/icono.png")
