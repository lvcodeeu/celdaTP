import pygame

from settings import Settings
from events import Eventos

class Graphic():
    """Una clase para almacenar las imagenes sueltas"""
    def __init__(self):
        """Inicia las imágenes a cargar en el juego"""
        self.settings = Settings()
        self.screen = self.settings.screen
        self.eventos = Eventos()
        #Inicio
        self.empezar_white = pygame.image.load("images/empezar_w.png")
        self.empezar_black = pygame.image.load("images/empezar_b.png")
        self.boton_empezar_rect = self.empezar_white.get_rect()
        self.empezar_xy = (350, 330)
        self.empezar_x = 350
        self.empezar_y = 330
        self.empezar_x2 = 615
        self.empezar_y2 = 372

    def boton_empezar(self):
        self.eventos.salir()
        self.screen.blit(self.empezar_white, (self.empezar_xy))
        self.posicion_raton_x, self.posicion_raton_y = pygame.mouse.get_pos()
        if self.posicion_raton_x > self.empezar_x and self.posicion_raton_x < self.empezar_x2:
            if self.posicion_raton_y > self.empezar_y and self.posicion_raton_y < self.empezar_y2:
                self.screen.blit(self.empezar_black, (self.empezar_xy))
        else:
            self.screen.blit(self.empezar_white, (self.empezar_xy))
