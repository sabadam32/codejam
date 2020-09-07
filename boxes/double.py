from boxes.box import Box


class DoubleBox(Box):

    def __init__(self):
        super().__init__(float)
        self.load_image('doublebox.png')

    def execute(self, data):
        valid_data = self.validate_input(data)
        if valid_data:
            return str(self.valid_input_type(data) * 2)
        return None
