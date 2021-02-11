import pygame, sys
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

        """Muertes"""
        #Chicle
        self.escena_muerte_chicle_1 = pygame.image.load("images/deaths/muerte_chicle1.png")
        self.escena_muerte_chicle_2 = pygame.image.load("images/deaths/muerte_chicle2.png")
        self.escena_muerte_chicle_3 = pygame.image.load("images/deaths/muerte_chicle3.png")
        self.escena_muerte_chicle_fin = pygame.image.load("images/deaths/muerte_chicle_fin.png")

        #tooltips
        self.clave_prota = 0
        self.tooltip_prota_activo = False
        self.clave_puerta = 1
        self.tooltip_puerta_activo = False
        self.clave_chicle = 2
        self.tooltip_chicle_activo = False
        self.clave_cajon = 3
        self.tooltip_cajon_activo = False
        self.clave_papel = 4
        self.tooltip_papel_activo = False
        self.clave_poster = 5
        self.tooltip_poster_activo = False

        #broma chicle
        self.contador_de_chicle = 0
        self.contador_imagenes_chicle = 1

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
        elif self.graphic_flag == 5:
            self.ventana_muerte_chicle()

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

    def ventana_muerte_chicle(self):
        """Crea la ventana para mostrar la muerte por chicle"""
        self.eventos.salir()
        if self.contador_imagenes_chicle == 1:
            self.settings.screen.blit(self.escena_muerte_chicle_1, (0, 0))
            self._avanzar_chicle()
        elif self.contador_imagenes_chicle == 2:
            self.settings.screen.blit(self.escena_muerte_chicle_2, (0, 0))
            self._avanzar_chicle()
        elif self.contador_imagenes_chicle == 3:
            self.settings.screen.blit(self.escena_muerte_chicle_3, (0, 0))
            self._avanzar_chicle()
        elif self.contador_imagenes_chicle == 4:
            self.settings.screen.blit(self.escena_muerte_chicle_fin, (0, 0))
            self._avanzar_chicle()
        elif self.contador_imagenes_chicle == 5:
            sys.exit()

    def _avanzar_chicle(self):
        """Avanza con la muerte del chicle"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.contador_imagenes_chicle += 1
                    self.ventana_muerte_chicle()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.contador_imagenes_chicle += 1
                    self.ventana_muerte_chicle()

    def _mensajes_info_ventana_carcel(self):
        """Genera los tooltips de la ventana_carcel"""
        #Protagonista
        self.detectar_raton_sobre_imagenes(self.settings.prota_x, self.settings.prota_x2, self.settings.prota_y, self.settings.prota_y2,
                                    self.narrativa.prota_tooltip, self.settings.barra_info_x, self.settings.barra_info_y,
                                    self.clave_prota)
        #Puerta
        self.detectar_raton_sobre_imagenes(self.settings.puerta_x, self.settings.puerta_x2, self.settings.puerta_y, self.settings.puerta_y2,
                                    self.narrativa.puerta_tooltip, self.settings.barra_info_x, self.settings.barra_info_y,
                                    self.clave_puerta)
        #Chicle
        self.detectar_raton_sobre_imagenes(self.settings.chicle_x, self.settings.chicle_x2, self.settings.chicle_y, self.settings.chicle_y2,
                                    self.narrativa.chicle_tooltip, self.settings.barra_info_x, self.settings.barra_info_y,
                                    self.clave_chicle)
        #Cajon
        self.detectar_raton_sobre_imagenes(self.settings.cajon_x, self.settings.cajon_x2, self.settings.cajon_y, self.settings.cajon_y2,
                                    self.narrativa.cajon_tooltip, self.settings.barra_info_x, self.settings.barra_info_y,
                                    self.clave_cajon)
        #Papel
        self.detectar_raton_sobre_imagenes(self.settings.papel_x, self.settings.papel_x2, self.settings.papel_y, self.settings.papel_y2,
                                    self.narrativa.papel_tooltip, self.settings.barra_info_x, self.settings.barra_info_y,
                                    self.clave_papel)
        #Poster
        self.detectar_raton_sobre_imagenes(self.settings.poster_x, self.settings.poster_x2, self.settings.poster_y, self.settings.poster_y2,
                                    self.narrativa.poster_tooltip, self.settings.barra_info_x, self.settings.barra_info_y,
                                    self.clave_poster)

    def detectar_raton_sobre_imagenes(self, posicion_x, posicion_x2, posicion_y, posicion_y2,
                                    texto_a_mostrar, posicion_x_impresion, posicion_y_impresion,
                                    selector_tooltip):
        """Detecta cuando el ratón está sobre algo para mostrar el tooltip"""
        self.posicion_raton_x, self.posicion_raton_y = pygame.mouse.get_pos()
        if self.posicion_raton_x > posicion_x and self.posicion_raton_x < posicion_x2:
            if self.posicion_raton_y > posicion_y and self.posicion_raton_y < posicion_y2:
                self.templates.generar_mensaje_info(texto_a_mostrar)
                self.dimension_x_texto, self.dimension_y_texto = self.templates.surface_texto.get_size()
                self.ubicacion_texto_tooltip_x = (posicion_x_impresion / 2) - (self.dimension_x_texto / 2) - 10
                self.settings.screen.blit(self.templates.surface_texto,(self.ubicacion_texto_tooltip_x, posicion_y_impresion))
                self.hacer_click_para_tooltip(selector_tooltip)

    def hacer_click_para_tooltip(self, selector_tooltip):
        """Muestra un tooltip flotante al hacer click"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self._reinicio_de_flotantes()
                self.justo_despues = self.secundero + 2
                if selector_tooltip == self.clave_prota:
                    self.contador_de_chicle = 0
                    self.tooltip_prota_activo = True
                elif selector_tooltip == self.clave_puerta:
                    self.contador_de_chicle = 0
                    self.tooltip_puerta_activo = True
                elif selector_tooltip == self.clave_chicle:
                    self.contador_de_chicle += 1
                    self.tooltip_chicle_activo = True
                elif selector_tooltip == self.clave_cajon:
                    self.contador_de_chicle = 0
                    self.tooltip_cajon_activo = True
                elif selector_tooltip == self.clave_papel:
                    self.contador_de_chicle = 0
                    self.tooltip_papel_activo = True
                elif selector_tooltip == self.clave_poster:
                    self.contador_de_chicle = 0
                    self.tooltip_poster_activo = True

    def generador_mensajes_flotantes(self):
        """Un generador con los distintos tooltips"""
        #prota
        if self.tooltip_prota_activo == True:
            self.mensaje_flotante(self.narrativa.prota_flotante)
            if self.secundero == self.justo_despues:
                self.tooltip_prota_activo = False
        #puerta
        elif self.tooltip_puerta_activo == True:
            self.mensaje_flotante(self.narrativa.puerta_flotante)
            if self.secundero == self.justo_despues:
                self.tooltip_puerta_activo = False
        #chicle
        elif self.tooltip_chicle_activo == True:
            if self.contador_de_chicle == 1:
                self.mensaje_flotante(self.narrativa.chicle_flotante)
                if self.secundero == self.justo_despues:
                    self.tooltip_chicle_activo = False
            if self.contador_de_chicle == 2:
                self.mensaje_flotante(self.narrativa.chicle_flotante_2)
                if self.secundero == self.justo_despues:
                    self.tooltip_chicle_activo = False
            if self.contador_de_chicle == 3:
                self.mensaje_flotante(self.narrativa.chicle_flotante_3)
                if self.secundero == self.justo_despues:
                    self.tooltip_chicle_activo = False
                    self.graphic_flag = 5
        #cajon
        elif self.tooltip_cajon_activo == True:
            self.mensaje_flotante(self.narrativa.cajon_flotante)
            if self.secundero == self.justo_despues:
                self.tooltip_cajon_activo = False
        #papel
        elif self.tooltip_papel_activo == True:
            self.mensaje_flotante(self.narrativa.papel_flotante)
            if self.secundero == self.justo_despues:
                self.tooltip_papel_activo = False
        #poster
        elif self.tooltip_poster_activo == True:
            self.mensaje_flotante(self.narrativa.poster_flotante)
            if self.secundero == self.justo_despues:
                self.tooltip_poster_activo = False

    def mensaje_flotante(self, texto_a_mostrar):
        """Muestra el mensaje flotante al producirse el evento MOUSEBUTTONDOWN"""
        self.templates.generar_mensaje_flotante_voz_prota(texto_a_mostrar)
        self.dimension_x_texto, self.dimension_y_texto = self.templates.surface_texto.get_size()
        self.ubicacion_texto_tooltip_x = (self.settings.flotante_x / 2) - (self.dimension_x_texto / 2)
        self.settings.screen.blit(self.templates.surface_texto,(self.ubicacion_texto_tooltip_x, self.settings.flotante_y))

    def _reinicio_de_flotantes(self):
        """Reinicia las flotantes para que funcione el contador del chicle"""
        self.tooltip_prota_activo = False
        self.tooltip_puerta_activo = False
        self.tooltip_chicle_activo = False
        self.tooltip_cajon_activo = False
        self.tooltip_papel_activo = False
        self.tooltip_poster_activo = False
