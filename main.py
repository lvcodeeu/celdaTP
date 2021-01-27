import pygame

from settings import Settings
from cursor import Cursor

class CeldaTP:
    """La clase principal para iniciar el juego"""
    def __init__(self):
        """Inicia el juego y crea los recursos"""
        pygame.init()

        self.settings = Settings()
        self.screen = self.settings.screen
        pygame.display.set_caption("celdaTP")
        pygame.display.set_icon(self.settings.icono)

        self.cursor = Cursor()

    def run_game(self):
        """Inicia el bucle principal del juego"""
        while True:
            self.show_game()
            self.eventos()

    def change_cursor(self):
        """Cambia el cursor normal por una mano"""
        self.cursor.cursor_image_rect.center = pygame.mouse.get_pos()
        self.screen.blit(self.cursor.cursor_image, self.cursor.cursor_image_rect.center)

    def show_game(self):
        """Muestra las pantallas del juego"""
        pygame.display.init()
        pygame.mouse.set_visible(False)
        self.screen.blit(self.settings.fondo_intro, (0, 0))
        self.change_cursor()
        pygame.display.flip()

    def eventos(self):
        """Define los eventos del ratón y teclado"""
        # teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == '__main__':
    celdatp = CeldaTP()
    celdatp.run_game()
