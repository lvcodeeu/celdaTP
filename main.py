import pygame
from datetime import datetime

from settings import Settings
from cursor import Cursor
from graphics import Graphic
from sounds import Sounds

class CeldaTP:
    """La clase principal para iniciar el juego"""
    def __init__(self):
        """Inicia el juego y crea los recursos"""
        pygame.mixer.pre_init(44100, 16, 2, 4096)

        self.clock = pygame.time.Clock()
        pygame.init()
        pygame.mixer.init()

        self.settings = Settings()
        self.screen = self.settings.screen
        pygame.display.set_caption("celdaTP")
        pygame.display.set_icon(self.settings.icono)

        self.cursor = Cursor()
        self.graphics = Graphic()
        self.sounds = Sounds()

    def run_game(self):
        """Inicia el bucle principal del juego"""
        self.sounds.intro_music()
        while True:
            self.show_game()

    def change_cursor(self):
        """Cambia el cursor normal por una mano"""
        self.cursor.cursor_image_rect.center = pygame.mouse.get_pos()
        self.screen.blit(self.cursor.cursor_image, self.cursor.cursor_image_rect.center)

    def show_game(self):
        """Muestra las pantallas del juego"""
        pygame.display.init()
        pygame.mouse.set_visible(False)
        self.graphics.ventana_actual()
        self.change_cursor()
        pygame.display.flip()

if __name__ == '__main__':
    celdatp = CeldaTP()
    celdatp.run_game()
