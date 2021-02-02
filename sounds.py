import os
import pygame

class Sounds():
    """Una clase para definir la música y los sonidos"""
    def __init__(self):
        """Inicia los valores de la clase Sounds"""


    def intro_music(self):
        """Activa la canción del inicio del juego"""
        pygame.mixer.music.load("sounds/intro.ogg")
        pygame.mixer.music.play(-1)
