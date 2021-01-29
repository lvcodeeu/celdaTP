import pygame

class Eventos():
    """Una clase para encapsular los eventos"""
    def __init__(self):
        """Inicia los eventos"""

    def salir(self):
        """Habilita la salida del juego"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
