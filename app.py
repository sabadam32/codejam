from os import path
import pygame
from pygame.locals import *
from resolution.screens import Standard
import boxes
import text.input
from text.labels import Label


class Application:
    def __init__(self, config):
        # Pygame Initialization
        pygame.init()

        # Application
        self._run = True
        self.level = 0
        self.info = config.get('info')
        self.screen = config.get('resolution', Standard.VGA)
        if pygame.font.get_init():
            font = config.get('font', {})
            self.font = font.get('name', 'Arial')
            self.font_size = font.get('font_size', 60)
        if self.info.get('title'):
            pygame.display.set_caption(self.info.get('title'))
        if self.info.get('logo'):
            pygame.display.set_icon(pygame.image.load(path.join('resources', 'img', self.info.get('logo'))))
        self.fps = config.get('display', {}).get('fps', 30)
        self.surface = pygame.display.set_mode(self.screen.size)
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load(path.join('resources', 'img', 'background.png')).convert()
        self.surface.blit(self.background, self.background.get_rect())
        self.text_input = text.input.TextInput(self.font, self.font_size)
        self.input_label = Label('Input: ', self.font, self.font_size, (10, 415))
        self.result_label = None
        self.levels = [boxes.DoubleBox(), boxes.AddAllDigits()]
        self.box = self.levels[self.level]

    def process_event(self, event):
        if event.type == pygame.QUIT:
            self._run = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_TAB:
                self.level += 1
                if self.level == len(self.levels):
                    self.level = 0
                self.box = self.levels[self.level]

    def update(self):
        pygame.display.update()

    def draw(self):
        self.surface.blit(self.background, self.background.get_rect())
        pygame.draw.rect(self.surface, (255,255,255), Rect(0, 400, 640, 480))
        self.box.draw()
        self.input_label.draw()
        self.draw_results()
        self.surface.blit(self.text_input.get_surface(), (self.input_label.text_size[0]+10, 415, 630, 470))

    def cleanup(self):
        pygame.quit()

    def new_label(self, text):
        return Label(text, self.font, self.font_size, (10, 10))

    def test_box(self, input):
        results = self.box.execute(input)
        if results:
            self.result_label = self.new_label(results)
        else:
            self.result_label = self.new_label('')

    def draw_results(self):
        if self.result_label:
            position = (10, 10)
            self.result_label.draw(position)

    def run(self):

        while self._run:
            events = pygame.event.get()
            for event in events:
                self.process_event(event)

                if self.text_input.update(events):
                    input = self.text_input.get_text()
                    self.text_input.clear_text()
                    self.test_box(input)

            self.draw()
            self.update()
            self.clock.tick(self.fps)
        self.cleanup()
