from boxes.box import Box
from pygame.rect import Rect


class DoubleBox(Box):

    def __init__(self):
        super().__init__('Double', 'Doubles input', Rect(75, 75, 100, 100), float)
        self.load_image('doublebox.png')

    def execute(self, data):
        valid_data = self.validate_input(data)
        if valid_data:
            return str(self.valid_input_type(data) * 2)
        return None
