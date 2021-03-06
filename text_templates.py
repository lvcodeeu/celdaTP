import pygame

from settings import Settings

class Templates:
    """Una clase para definir plantillas de texto"""
    def __init__(self):
        """Inicia los valores de las plantillas"""
        self.settings = Settings()

    def plantilla_mostrar_textos(self, texto_a_mostrar):
        """Genera una plantilla para renderizar los textos, a falta de usar blit() para mostrarlos"""
        self.fuente_del_texto = pygame.font.Font("fonts/nimbus_mono_l.ttf", 20)
        self.surface_texto = self.fuente_del_texto.render(texto_a_mostrar, False, (self.settings.texto_naranja))

    def generar_mensaje_flotante_voz_prota(self, texto_a_mostrar):
        """Genera una plantilla para renderizar los textos flotantes, a falta de usar blit() para mostrarlos"""
        self.fuente_del_texto = pygame.font.SysFont("Console", 15)
        self.surface_texto = self.fuente_del_texto.render(texto_a_mostrar, False, (self.settings.texto_blanco))

    def generar_mensaje_info(self, texto_a_mostrar):
        """Genera una plantilla para renderizar los textos informativos, a falta de usar blit() para mostrarlos"""
        self.fuente_del_texto = pygame.font.SysFont("Console", 15)
        self.surface_texto = self.fuente_del_texto.render(texto_a_mostrar, False, (self.settings.texto_amarillo))
