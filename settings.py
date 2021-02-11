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

        #Color de los textos
        self.texto_naranja = (200, 70, 10)
        self.texto_blanco = (255, 255, 255)
        self.texto_amarillo = (160, 190, 0)

        # Márgenes
        self.margen_x = 80
        self.margen_y = 80
        self.margen_x2 = 880
        self.margen_y2 = 460

        """Posiciones"""
        #Botón empezar
        self.empezar_x = 350
        self.empezar_y = 440
        self.empezar_x2 = 609
        self.empezar_y2 = 483
        self.empezar_xy = (self.empezar_x, self.empezar_y)

        #Posicion texto flotante
        self.flotante_x = 960
        self.flotante_y = 30

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

        #Posicion texto barra info
        self.barra_info_x = 960
        self.barra_info_y = 390

        #Posiciones ventana_carcel
        self.prota_x = 705
        self.prota_x2 = 820
        self.prota_y = 234
        self.prota_y2 = 342
        self.papel_x = 105
        self.papel_x2 = 170
        self.papel_y = 210
        self.papel_y2 = 240
        self.cajon_x = 190
        self.cajon_x2 = 230
        self.cajon_y = 245
        self.cajon_y2 = 282
        self.chicle_x = 240
        self.chicle_x2 = 250
        self.chicle_y = 205
        self.chicle_y2 = 215
        self.puerta_x = 535
        self.puerta_x2 = 660
        self.puerta_y = 0
        self.puerta_y2 = 280
        self.poster_x = 842
        self.poster_x2 = 913
        self.poster_y = 70
        self.poster_y2 = 240
