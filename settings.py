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
        self.icono = pygame.image.load("images/buttons/icono.png")

        #Color naranja de los textos
        self.texto_naranja = (200, 70, 10)

        # Márgenes
        self.margen_x = 80
        self.margen_y = 80
        self.margen_x2 = 880
        self.margen_y2 = 460

        #Botón empezar
        self.empezar_x = 350
        self.empezar_y = 440
        self.empezar_x2 = 609
        self.empezar_y2 = 483
        self.empezar_xy = (self.empezar_x, self.empezar_y)

        #Posiciones textos presentación
        self.posicion_y_2 = 130
        self.posicion_y_3 = 155
        self.posicion_y_4 = 205
        self.posicion_y_5 = 230
        self.posicion_y_6 = 255
        self.posicion_y_7 = 305
        self.posicion_y_8 = 355
        self.posicion_y_9 = 380
        self.posicion_y_10 = 455
        self.posicion_x_flecha = 20
        self.posicion_y_flecha = 412
        self.posicion_y_nombre = 405
        self.posicion_x_tecla_incorrecta = 80
        self.posicion_y_tecla_incorrecta = 450
