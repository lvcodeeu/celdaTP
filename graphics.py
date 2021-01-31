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
        self.eventos = Eventos()
        self.narrativa = Narrativa()
        self.player = Player()

        #Inicio
        self.graphic_flag = 1
        self.fondo_intro = pygame.image.load("images/intro.png")
        self.empezar_white = pygame.image.load("images/empezar_w.png")
        self.empezar_black = pygame.image.load("images/empezar_b.png")
        self.boton_empezar_rect = self.empezar_white.get_rect()
        self.empezar_x = 350
        self.empezar_y = 440
        self.empezar_x2 = 609
        self.empezar_y2 = 483
        self.empezar_xy = (self.empezar_x, self.empezar_y)

        #presentacion
        self.fondo_presentacion = pygame.image.load("images/fondo_presentacion.png")

    def ventana_actual(self):
        """Es la ventana que se muestra en todo momento"""
        if self.graphic_flag == 1:
            self.ventana_inicio()
        elif self.graphic_flag == 2:
            self.ventana_presentacion()
        elif self.graphic_flag == 3:
            self.ventana_presentacion_nombre()
        elif self.graphic_flag == 4:
            self.ventana_carcel()

    def ventana_inicio(self):
        """Crea la pantalla inicial y el boton empezar e incluye el cambio de color al posar el raton"""
        self.eventos.salir()
        self.settings.screen.blit(self.fondo_intro, (0, 0))
        self.settings.screen.blit(self.empezar_white, (self.empezar_xy))
        self.posicion_raton_x, self.posicion_raton_y = pygame.mouse.get_pos()
        #cambiar color del boton empezar
        if self.posicion_raton_x > self.empezar_x and self.posicion_raton_x < self.empezar_x2:
            if self.posicion_raton_y > self.empezar_y and self.posicion_raton_y < self.empezar_y2:
                self.settings.screen.blit(self.empezar_black, (self.empezar_xy))
                #activar el boton
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.graphic_flag = 2
        else:
            self.settings.screen.blit(self.empezar_white, (self.empezar_xy))

    def ventana_presentacion(self):
        """Crea la pantalla de presentacion"""
        self.eventos.salir()
        self.settings.screen.blit(self.fondo_presentacion, (0, 0))
        self.narrativa.mostrar_textos_presentacion()
        self.player.pedir_nombre_jugador()
        if self.player.nombre_introducido == True:
            self.graphic_flag = 3

    def ventana_presentacion_nombre(self):
        """Crea la pantalla con la coña sobre el nombre"""
        self.eventos.salir()
        self.settings.screen.blit(self.fondo_presentacion, (0, 0))
        self.player.mostrar_ultimos_textos_presentacion()
        self.narrativa.bromear_con_nombre()
        self.eventos.hacer_click_para_continuar()
        if self.eventos.click_para_continuar == True:
            self.graphic_flag = 4

    def ventana_carcel(self):
        """Crea la ventana de inicio en la cárcel"""
        self.eventos.salir()
        self.settings.screen.blit(self.fondo_presentacion, (0, 0))
