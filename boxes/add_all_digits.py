from boxes.box import Box
from pygame.rect import Rect


class AddAllDigits(Box):

    def __init__(self):
        super().__init__('Add All Digits', 'Adds up all the numbers found in the input string', Rect(75, 75, 100, 100), str)
        self.load_image('box.png')

    def execute(self, data):
        contains_digit = any(map(str.isdigit, data))
        if contains_digit:
            sum = 0
            for char in data:
                if char.isdigit():
                    sum += int(char)
            return str(sum)
        return '0'
