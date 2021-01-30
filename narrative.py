import pygame

from settings import Settings
from events import Eventos
from player import Player

class Narrativa():
    """Una clase para almacenar los textos del juego"""
    def __init__(self):
        """Inicia los valores de los textos"""
        self.settings = Settings()
        self.screen = self.settings.screen
        self.eventos = Eventos()
        self.player = Player()

        self.text_flag = 1
        #Presentacion
        self.presentacion_1 = "Bienvenido al juego de aventuras CeldaTP"
        self.presentacion_2 = "Una historia en la que puedes encontrar a tu yo interior"
        self.presentacion_3 = "o a mi tu exterior, o al otro que entra y sale."
        self.presentacion_4 = "¿Crees que puedes conseguir terminar el juego?"
        self.presentacion_5 = "Te reto a que seas sincero, y compruebes en realidad hasta"
        self.presentacion_6 = "dónde eres capaz de llegar."
        self.presentacion_7 = "¡Buena suerte! (la vas a necesitar…)"
        self.presentacion_8 = "En primer lugar, dime tu nombre:"
        self.presentacion_9 = "aqui hay que meter el nombre del jugador"
        self.presentacion_10 = "Vaya, ¿te llamas " + self.player.nombre_jugador + "?"
        self.flecha_derecha = pygame.image.load("images/right_arrow_white.png")
        self.mensaje_error_en_la_tecla = "Si tocas esa tecla otra vez se puede destruir el juego."

    def mostrar_textos_presentacion(self):
        """Muestra los textos de la presentacion"""
        pygame.font.init()
        self.plantilla_mostrar_textos(self.presentacion_1)
        self.screen.blit(self.surface_texto,(self.settings.margen_x,self.settings.margen_y))
        self.plantilla_mostrar_textos(self.presentacion_2)
        self.screen.blit(self.surface_texto,(self.settings.margen_x,self.settings.posicion_y_2))
        self.plantilla_mostrar_textos(self.presentacion_3)
        self.screen.blit(self.surface_texto,(self.settings.margen_x,self.settings.posicion_y_3))
        self.plantilla_mostrar_textos(self.presentacion_4)
        self.screen.blit(self.surface_texto,(self.settings.margen_x,self.settings.posicion_y_4))
        self.plantilla_mostrar_textos(self.presentacion_5)
        self.screen.blit(self.surface_texto,(self.settings.margen_x,self.settings.posicion_y_5))
        self.plantilla_mostrar_textos(self.presentacion_6)
        self.screen.blit(self.surface_texto,(self.settings.margen_x,self.settings.posicion_y_6))
        self.plantilla_mostrar_textos(self.presentacion_7)
        self.screen.blit(self.surface_texto,(self.settings.margen_x,self.settings.posicion_y_7))
        self.plantilla_mostrar_textos(self.presentacion_8)
        self.screen.blit(self.surface_texto,(self.settings.margen_x,self.settings.posicion_y_8))
        self.screen.blit(self.flecha_derecha, (self.settings.posicion_x_flecha, self.settings.posicion_y_flecha))
        if self.player.nombre_introducido == True:
            self.mostrar_textos_presentacion()

    def mostrar_ultimos_textos_presentacion(self):
        """Muestra la parte final de la presentacion"""
        self.plantilla_mostrar_textos(self.presentacion_10)
        self.screen.blit(self.surface_texto,(self.settings.margen_x,self.settings.posicion_y_10))
        print(self.player.nombre_jugador)

    def plantilla_mostrar_textos(self, texto_a_mostrar):
        """Genera una plantilla para renderizar los textos, a falta de usar blit() para mostrarlos"""
        self.fuente_del_texto = pygame.font.SysFont('Nimbus Mono PS Italic', 30)
        self.surface_texto = self.fuente_del_texto.render(texto_a_mostrar, False, (255, 255, 255))
