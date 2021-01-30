import pygame

class Player():
    """Una clase con los parámetros del jugador"""
    def __init__(self):
        """Inicia los parámetros del jugador"""
        self.nombre_jugador = []

    def pedir_nombre_jugador(self):
        """Solicita el nombre al jugador y lo guarda en una cadena"""
        for event in pygame.event.get():
            if event.type == pygame.K_a:
                self.nombre_jugador.append("A")
            elif event.type == pygame.K_b:
                self.nombre_jugador.append("B")
            elif event.type == pygame.K_c:
                self.nombre_jugador.append("C")
            elif event.type == pygame.K_d:
                self.nombre_jugador.append("D")
            elif event.type == pygame.K_e:
                self.nombre_jugador.append("E")
            elif event.type == pygame.K_f:
                self.nombre_jugador.append("F")
            elif event.type == pygame.K_g:
                self.nombre_jugador.append("G")
            elif event.type == pygame.K_h:
                self.nombre_jugador.append("H")
            elif event.type == pygame.K_i:
                self.nombre_jugador.append("I")
            elif event.type == pygame.K_j:
                self.nombre_jugador.append("J")
            elif event.type == pygame.K_k:
                self.nombre_jugador.append("K")
            elif event.type == pygame.K_l:
                self.nombre_jugador.append("L")
            elif event.type == pygame.K_m:
                self.nombre_jugador.append("M")
            elif event.type == pygame.K_n:
                self.nombre_jugador.append("N")
            elif event.type == pygame.K_o:
                self.nombre_jugador.append("O")
            elif event.type == pygame.K_p:
                self.nombre_jugador.append("P")
            elif event.type == pygame.K_q:
                self.nombre_jugador.append("Q")
            elif event.type == pygame.K_r:
                self.nombre_jugador.append("R")
            elif event.type == pygame.K_s:
                self.nombre_jugador.append("S")
            elif event.type == pygame.K_t:
                self.nombre_jugador.append("T")
            elif event.type == pygame.K_u:
                self.nombre_jugador.append("U")
            elif event.type == pygame.K_v:
                self.nombre_jugador.append("V")
            elif event.type == pygame.K_w:
                self.nombre_jugador.append("W")
            elif event.type == pygame.K_X:
                self.nombre_jugador.append("X")
            elif event.type == pygame.K_Y:
                self.nombre_jugador.append("Y")
            elif event.type == pygame.K_Z:
                self.nombre_jugador.append("Z")
            elif event.type == pygame.K_BACKSPACE:
                self.nombre_jugador.append(" ")
            elif event.type == pygame.K_BACKSLASH:
                self.nombre_jugador.pop()
            else:
                self.aviso_tecla_incorrecta()

    def aviso_tecla_incorrecta(self):
        """Indica al usuario que la tecla introducida no es válida"""
        print("La tecla pulsada no es válida")
