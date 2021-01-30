import pygame

class Settings:
    """ Una clase para almacenar la configuración de celdaTP """

    def __init__(self):
        """ Inicializa la configuración del juego """

        # Configuración de pantalla
        self.screen_width = 960
        self.screen_height = 540
        self.screen = pygame.display.set_mode((self.screen_width,
                                              self.screen_height))
        self.icono = pygame.image.load("images/icono.png")

        # Margenes
        self.margen_x = 80
        self.margen_y = 80
        self.margen_x2 = 880
        self.margen_y2 = 460
