import pygame

class Eventos():
    """Una clase para encapsular los eventos"""
    def __init__(self):
        """Inicia los eventos"""
        self.click_para_continuar = False

    def salir(self):
        """Habilita la salida del juego"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def hacer_click_para_continuar(self):
        """Pausa el juego hasta que el jugador hace click en el ratón para continuar"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click_para_continuar = True
