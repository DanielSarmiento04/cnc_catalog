from kivy.uix.button import Button


class LightButton(Button):
    """Button with light theme"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (0.9, 0.9, 0.9, 1)  # Light gray background
        self.color = (0, 0, 0, 1)  # Black text
