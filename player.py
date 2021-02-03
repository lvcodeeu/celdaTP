import pygame

from settings import Settings
from text_templates import Templates

class Player():
    """Una clase con los parámetros del jugador"""
    def __init__(self):
        """Inicia los parámetros del jugador"""
        self.settings = Settings()
        self.templates = Templates()
        self.nombre_jugador_list = []
        self.nombre_jugador = ""
        self.nombre_introducido = False
        self.tecla_pulsada = pygame.key.get_pressed()
        self.imagen_tecla_incorrecta = pygame.image.load("images/tecla_incorrecta.png")
        self.frames_counter = 0
        self.tecla_incorrecta = False

    def pedir_nombre_jugador(self):
        """Solicita el nombre al jugador y lo guarda en una cadena"""
        self.mostrar_aviso_tecla_incorrecta()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.nombre_jugador_list.append("A")
                elif event.key == pygame.K_b:
                    self.nombre_jugador_list.append("B")
                elif event.key == pygame.K_c:
                    self.nombre_jugador_list.append("C")
                elif event.key == pygame.K_d:
                    self.nombre_jugador_list.append("D")
                elif event.key == pygame.K_e:
                    self.nombre_jugador_list.append("E")
                elif event.key == pygame.K_f:
                    self.nombre_jugador_list.append("F")
                elif event.key == pygame.K_g:
                    self.nombre_jugador_list.append("G")
                elif event.key == pygame.K_h:
                    self.nombre_jugador_list.append("H")
                elif event.key == pygame.K_i:
                    self.nombre_jugador_list.append("I")
                elif event.key == pygame.K_j:
                    self.nombre_jugador_list.append("J")
                elif event.key == pygame.K_k:
                    self.nombre_jugador_list.append("K")
                elif event.key == pygame.K_l:
                    self.nombre_jugador_list.append("L")
                elif event.key == pygame.K_m:
                    self.nombre_jugador_list.append("M")
                elif event.key == pygame.K_n:
                    self.nombre_jugador_list.append("N")
                elif event.key == pygame.K_o:
                    self.nombre_jugador_list.append("O")
                elif event.key == pygame.K_p:
                    self.nombre_jugador_list.append("P")
                elif event.key == pygame.K_q:
                    self.nombre_jugador_list.append("Q")
                elif event.key == pygame.K_r:
                    self.nombre_jugador_list.append("R")
                elif event.key == pygame.K_s:
                    self.nombre_jugador_list.append("S")
                elif event.key == pygame.K_t:
                    self.nombre_jugador_list.append("T")
                elif event.key == pygame.K_u:
                    self.nombre_jugador_list.append("U")
                elif event.key == pygame.K_v:
                    self.nombre_jugador_list.append("V")
                elif event.key == pygame.K_w:
                    self.nombre_jugador_list.append("W")
                elif event.key == pygame.K_x:
                    self.nombre_jugador_list.append("X")
                elif event.key == pygame.K_y:
                    self.nombre_jugador_list.append("Y")
                elif event.key == pygame.K_z:
                    self.nombre_jugador_list.append("Z")
                elif event.key == pygame.K_SPACE:
                    self.nombre_jugador_list.append(" ")
                elif event.key == pygame.K_BACKSPACE:
                    del self.nombre_jugador_list[-1]
                elif event.key == pygame.K_RETURN:
                    self.nombre_introducido = True
                else:
                    self.tecla_incorrecta = True
                    self.mostrar_aviso_tecla_incorrecta()
        self.nombre_jugador = "".join(self.nombre_jugador_list)
        self.templates.plantilla_mostrar_textos(self.nombre_jugador)
        self.settings.screen.blit(self.templates.surface_texto,(self.settings.margen_x,self.settings.posicion_y_nombre))

    def mostrar_ultimos_textos_presentacion(self):
        """Muestra la parte final de la presentacion"""
        if self.nombre_introducido == True:
            self.presentacion_10 = "Vaya, ¿te llamas %s?" %self.nombre_jugador
            self.templates.plantilla_mostrar_textos(self.presentacion_10)
            self.settings.screen.blit(self.templates.surface_texto,(self.settings.margen_x,self.settings.margen_y))

    def mostrar_aviso_tecla_incorrecta(self):
        """Muestra la imagen de tecla incorrecta"""
        if self.tecla_incorrecta == True:
            self.settings.screen.blit(self.imagen_tecla_incorrecta,(self.settings.posicion_x_tecla_incorrecta,self.settings.posicion_y_tecla_incorrecta))
            self.frames_counter += 1
        self.aviso_tecla_incorrecta()

    def aviso_tecla_incorrecta(self):
        """Indica al usuario que la tecla introducida no es válida"""
        if self.frames_counter >= 60:
            self.frames_counter = 0
            self.tecla_incorrecta = False
