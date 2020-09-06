import pygame


class Label:

    def __init__(self, text, font, size, position):
        self.label = text
        self.size = size
        self.screen = pygame.display.get_surface()
        if pygame.font.get_init():
            self.font = pygame.font.SysFont(font, size)
        self.position = position
        self.screen = pygame.display.get_surface()
        self.surface = self.font.render(self.label, False, (0, 0, 0))
        self.text_size = self.font.size(text)

    def draw(self, position=None):
        if position is None:
            position = self.position
        self.screen.blit(self.surface, position)
