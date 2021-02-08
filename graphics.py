import pygame
import datetime

from settings import Settings
from events import Eventos
from narrative import Narrativa
from player import Player
from text_templates import Templates

class Graphic():
    """Una clase para gestionar las imagenes"""
    def __init__(self):
        """Inicia las imágenes a cargar en el juego"""
        self.settings = Settings()
        self.eventos = Eventos()
        self.narrativa = Narrativa()
        self.player = Player()
        self.templates = Templates()

        #Inicio
        self.graphic_flag = 1
        self.fondo_intro = pygame.image.load("images/backgrounds/intro.png")
        self.empezar_white = pygame.image.load("images/buttons/empezar_w.png")
        self.empezar_black = pygame.image.load("images/buttons/empezar_b.png")
        self.boton_empezar_rect = self.empezar_white.get_rect()

        #presentacion
        self.fondo_presentacion = pygame.image.load("images/backgrounds/fondo_presentacion.png")

        #escena_celda
        self.escena_celda = pygame.image.load("images/backgrounds/escena_celda.png")

        #tooltips
        self.tooltip_prota_activo = False
        self.frames_counter = 0

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
            self.secundero = int(datetime.datetime.utcnow().timestamp())
            self._mensajes_info_ventana_carcel()
            self.generador_mensajes_flotantes()

    def ventana_inicio(self):
        """Crea la pantalla inicial y el boton empezar e incluye el cambio de color al posar el raton"""
        self.eventos.salir()
        self.settings.screen.blit(self.fondo_intro, (0, 0))
        self.settings.screen.blit(self.empezar_white, (self.settings.empezar_xy))
        #cambiar color del boton empezar
        self.posicion_raton_x, self.posicion_raton_y = pygame.mouse.get_pos()
        if self.posicion_raton_x > self.settings.empezar_x and self.posicion_raton_x < self.settings.empezar_x2:
            if self.posicion_raton_y > self.settings.empezar_y and self.posicion_raton_y < self.settings.empezar_y2:
                self.settings.screen.blit(self.empezar_black, (self.settings.empezar_xy))
                #activar el boton
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.graphic_flag = 2
        else:
            self.settings.screen.blit(self.empezar_white, (self.settings.empezar_xy))

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
        self.settings.screen.blit(self.escena_celda, (0, 0))

    def _mensajes_info_ventana_carcel(self):
        """Genera los tooltips de la ventana_carcel"""
        #Protagonista
        self.detectar_raton_sobre_imagenes(self.settings.prota_x, self.settings.prota_x2, self.settings.prota_y, self.settings.prota_y2,
                                    self.narrativa.prota_tooltip, self.settings.barra_info_x, self.settings.barra_info_y)

    def detectar_raton_sobre_imagenes(self, posicion_x, posicion_x2, posicion_y, posicion_y2,
                                    texto_a_mostrar, posicion_x_impresion, posicion_y_impresion):
        """Detecta cuando el ratón está sobre algo para mostrar el tooltip"""
        self.posicion_raton_x, self.posicion_raton_y = pygame.mouse.get_pos()
        if self.posicion_raton_x > posicion_x and self.posicion_raton_x < posicion_x2:
            if self.posicion_raton_y > posicion_y and self.posicion_raton_y < posicion_y2:
                self.templates.generar_mensaje_info(texto_a_mostrar)
                self.dimension_x_texto, self.dimension_y_texto = self.templates.surface_texto.get_size()
                self.ubicacion_texto_tooltip_x = (posicion_x_impresion / 2) - (self.dimension_x_texto / 2)
                self.settings.screen.blit(self.templates.surface_texto,(self.ubicacion_texto_tooltip_x, posicion_y_impresion))
                self.hacer_click_para_tooltip()

    def hacer_click_para_tooltip(self):
        """Muestra un tooltip flotante al hacer click"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.justo_despues = self.secundero + 2
                self.tooltip_prota_activo = True

    def generador_mensajes_flotantes(self):
        """Un generador con los distintos tooltips"""
        if self.tooltip_prota_activo == True:
            self.mensaje_flotante(self.narrativa.prota_flotante)
            if self.secundero == self.justo_despues:
                self.tooltip_prota_activo = False

    def mensaje_flotante(self, texto_a_mostrar):
        """Muestra el mensaje flotante al producirse el evento MOUSEBUTTONDOWN"""
        self.templates.generar_mensaje_flotante_voz_prota(texto_a_mostrar)
        self.settings.screen.blit(self.templates.surface_texto,(self.settings.flotante_x, self.settings.flotante_y))
