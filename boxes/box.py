import pygame
from os import path


class Box:

    def __init__(self, name, function, size_rect, input_type):
        self.name = name
        self.function = function
        self.size_rect = size_rect
        self.screen = pygame.display.get_surface()
        self.valid_input_type = input_type
        self.box_img = None
        self.box_rect = None

    def load_image(self, image):
        self.box_img = pygame.image.load(path.join('resources', 'img', image)).convert()
        self.box_rect = self.box_img.get_rect()
        self.box_rect.center = 320, 200

    def validate_input(self, input):
        try:
            return self.valid_input_type(input)
        except ValueError:
            return None

    def draw(self):
        self.screen.blit(self.box_img, self.box_rect)
