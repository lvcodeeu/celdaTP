import pygame

from settings import Settings
from events import Eventos
from narrative import Narrativa
from player import Player

class Graphic():
    """Una clase para almacenar las imagenes sueltas"""
    def __init__(self):
        """Inicia las imágenes a cargar en el juego"""
        self.settings = Settings()
        self.screen = self.settings.screen
        self.eventos = Eventos()
        self.narrativa = Narrativa()
        self.player = Player()

        #Inicio
        self.graphic_flag = 1
        self.fondo_intro = pygame.image.load("images/intro.png")
        self.empezar_white = pygame.image.load("images/empezar_w.png")
        self.empezar_black = pygame.image.load("images/empezar_b.png")
        self.boton_empezar_rect = self.empezar_white.get_rect()
        self.empezar_xy = (350, 330)
        self.empezar_x = 350
        self.empezar_y = 330
        self.empezar_x2 = 615
        self.empezar_y2 = 372

        #presentacion
        self.fondo_presentacion = pygame.image.load("images/fondo_presentacion.png")

    def ventana_actual(self):
        """Es la ventana que se muestra en todo momento"""
        if self.graphic_flag == 1:
            self.ventana_inicio()
        elif self.graphic_flag == 2:
            self.ventana_presentacion()

    def ventana_inicio(self):
        """Crea la pantalla inicial y el boton empezar e incluye el cambio de color al posar el raton"""
        self.eventos.salir()
        self.screen.blit(self.fondo_intro, (0, 0))
        self.screen.blit(self.empezar_white, (self.empezar_xy))
        self.posicion_raton_x, self.posicion_raton_y = pygame.mouse.get_pos()
        #cambiar color del boton empezar
        if self.posicion_raton_x > self.empezar_x and self.posicion_raton_x < self.empezar_x2:
            if self.posicion_raton_y > self.empezar_y and self.posicion_raton_y < self.empezar_y2:
                self.screen.blit(self.empezar_black, (self.empezar_xy))
                #activar el boton
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #self.ventana_presentacion()
                        self.graphic_flag = 2
        else:
            self.screen.blit(self.empezar_white, (self.empezar_xy))

    def ventana_presentacion(self):
        """Crea la pantalla de presentacion"""
        self.eventos.salir()
        self.screen.blit(self.fondo_presentacion, (0, 0))
        self.narrativa.mostrar_textos_presentacion()
        #aqui hay que mostrar el cajetin para que escriba el nombre
        self.player.pedir_nombre_jugador()
