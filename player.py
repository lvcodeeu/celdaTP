import pygame

from settings import Settings

class Player():
    """Una clase con los parámetros del jugador"""
    def __init__(self):
        """Inicia los parámetros del jugador"""
        self.settings = Settings()

        self.nombre_jugador_list = []
        self.nombre_jugador = ""
        self.tecla_pulsada = pygame.key.get_pressed()
        self.tecla_incorrecta = False
        self.nombre_introducido = False

    def pedir_nombre_jugador(self):
        """Solicita el nombre al jugador y lo guarda en una cadena"""
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
                    self.aviso_tecla_incorrecta()
        self.nombre_jugador = "".join(self.nombre_jugador_list)
        self.fuente_del_texto = pygame.font.SysFont('Nimbus Mono PS Italic', 30)
        self.surface_texto = self.fuente_del_texto.render(self.nombre_jugador, False, (255, 255, 255))
        self.settings.screen.blit(self.surface_texto,(self.settings.margen_x,self.settings.posicion_y_nombre))

    def aviso_tecla_incorrecta(self):
        """Indica al usuario que la tecla introducida no es válida"""
        print("La tecla pulsada no es válida")
        self.tecla_incorrecta = True