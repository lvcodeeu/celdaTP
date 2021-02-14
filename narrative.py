import pygame
import random

from settings import Settings
from events import Eventos
from player import Player
from text_templates import Templates

class Narrativa():
    """Una clase para almacenar los textos del juego"""
    def __init__(self):
        """Inicia los valores de los textos"""
        self.settings = Settings()
        self.eventos = Eventos()
        self.player = Player()
        self.templates = Templates()

        self.text_flag = 1

        #Presentacion
        self.presentacion_1 = "Bienvenido al juego de aventuras CeldaTP"
        self.presentacion_2 = "Una historia en la que puedes encontrar a tu yo interior"
        self.presentacion_3 = "o a mi tu exterior, o al otro que entra y sale."
        self.presentacion_4 = "¿Crees que puedes conseguir terminar el juego?"
        self.presentacion_5 = "Te reto a que seas sincero, y compruebes en realidad hasta dónde"
        self.presentacion_6 = "eres capaz de llegar."
        self.presentacion_7 = "¡Buena suerte! (la vas a necesitar…)"
        self.presentacion_8 = "En primer lugar, dime tu nombre, y pulsa Enter:"
        self.presentacion_9 = "aqui hay que meter el nombre del jugador"
        self.flecha_derecha = pygame.image.load("images/buttons/right_arrow_orange.png")
        self.mensaje_error_en_la_tecla = "Si tocas esa tecla otra vez se puede destruir el juego."
        self.presentacion_final = "En cualquier caso, la historia comienza así..."

        #Bromas nombre
        self.numero_respuesta = random.randint(1, 5)
        self.broma_nombre_1 = "Yo tuve un perro que se llamaba igual."
        self.broma_nombre_2 = "¿Así no se llama una comida búlgara que huele muy mal?"
        self.broma_nombre_3 = "Con ese nombre no quiero ni imaginarme tu cara."
        self.broma_nombre_4 = "Qué nombre más feo. Te compadezco."
        self.broma_nombre_5 = "¿No serás familia del tío ese tan raro que sale por la tele?"
        self.broma_finalizada = False

        #Tooltips ventana_carcel
        self.prota_tooltip = "Ese eres tú"
        self.poster_tooltip = "Póster sensual"
        self.papel_tooltip = "Carta manuscrita"
        self.cajon_tooltip = "Cajón de la mesa"
        self.chicle_tooltip = "Chicle mordisqueado asqueroso"
        self.puerta_tooltip = "Puerta de la celda"

        #Mensajes flotantes ventana_carcel
        self.prota_flotante = "¿Cómo habré llegado hasta aquí?"
        self.cajon_flotante = "El cajón está cerrado."
        self.chicle_flotante = "No pienso tocar eso."
        self.chicle_flotante_2 = "En serio, no me hagas tocarlo."
        self.chicle_flotante_3 = "Vale, me lo como."
        self.puerta_flotante = "No puedo abrir la puerta. Está cerrada con llave."

        #Tooltips ventana_poster
        self.poster_poster_tooltip = "Mujer preciosa"
        self.poster_chincheta_tooltip = "Chincheta medio suelta"

        #Mensajes flotantes ventana_poster
        self.poster_poster_flotante = "Tengo la impresión de estar encadenado perpetuamente."
        self.poster_chincheta_flotante = "Esta chincheta parece un poco suelta. Igual si tiro de ella..."
        self.poster_chincheta_flotante_2 = "Vale. La arranco."


    def mostrar_textos_presentacion(self):
        """Muestra los textos de la presentacion"""
        pygame.font.init()
        self.templates.plantilla_mostrar_textos(self.presentacion_1)
        self.settings.screen.blit(self.templates.surface_texto,(self.settings.margen_x,self.settings.margen_y))
        self.templates.plantilla_mostrar_textos(self.presentacion_2)
        self.settings.screen.blit(self.templates.surface_texto,(self.settings.margen_x,self.settings.posicion_y_2))
        self.templates.plantilla_mostrar_textos(self.presentacion_3)
        self.settings.screen.blit(self.templates.surface_texto,(self.settings.margen_x,self.settings.posicion_y_3))
        self.templates.plantilla_mostrar_textos(self.presentacion_4)
        self.settings.screen.blit(self.templates.surface_texto,(self.settings.margen_x,self.settings.posicion_y_4))
        self.templates.plantilla_mostrar_textos(self.presentacion_5)
        self.settings.screen.blit(self.templates.surface_texto,(self.settings.margen_x,self.settings.posicion_y_5))
        self.templates.plantilla_mostrar_textos(self.presentacion_6)
        self.settings.screen.blit(self.templates.surface_texto,(self.settings.margen_x,self.settings.posicion_y_6))
        self.templates.plantilla_mostrar_textos(self.presentacion_7)
        self.settings.screen.blit(self.templates.surface_texto,(self.settings.margen_x,self.settings.posicion_y_7))
        self.templates.plantilla_mostrar_textos(self.presentacion_8)
        self.settings.screen.blit(self.templates.surface_texto,(self.settings.margen_x,self.settings.posicion_y_8))
        self.settings.screen.blit(self.flecha_derecha, (self.settings.posicion_x_flecha, self.settings.posicion_y_flecha))

    def bromear_con_nombre(self):
        """Genera la broma con el nombre"""
        if self.numero_respuesta == 1:
            self.templates.plantilla_mostrar_textos(self.broma_nombre_1)
            self.settings.screen.blit(self.templates.surface_texto,(self.settings.margen_x,self.settings.posicion_y_2))
        if self.numero_respuesta == 2:
            self.templates.plantilla_mostrar_textos(self.broma_nombre_2)
            self.settings.screen.blit(self.templates.surface_texto,(self.settings.margen_x,self.settings.posicion_y_2))
        if self.numero_respuesta == 3:
            self.templates.plantilla_mostrar_textos(self.broma_nombre_3)
            self.settings.screen.blit(self.templates.surface_texto,(self.settings.margen_x,self.settings.posicion_y_2))
        if self.numero_respuesta == 4:
            self.templates.plantilla_mostrar_textos(self.broma_nombre_4)
            self.settings.screen.blit(self.templates.surface_texto,(self.settings.margen_x,self.settings.posicion_y_2))
        if self.numero_respuesta == 5:
            self.templates.plantilla_mostrar_textos(self.broma_nombre_5)
            self.settings.screen.blit(self.templates.surface_texto,(self.settings.margen_x,self.settings.posicion_y_2))

        self.templates.plantilla_mostrar_textos(self.presentacion_final)
        self.settings.screen.blit(self.templates.surface_texto,(self.settings.margen_x,self.settings.posicion_y_3))
