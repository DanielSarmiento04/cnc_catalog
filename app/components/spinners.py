from kivy.uix.spinner import Spinner


class LightSpinner(Spinner):
    """Spinner with light theme"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (0.9, 0.9, 0.9, 1)  # Light gray background
        self.color = (0, 0, 0, 1)  # Black text
        self.option_cls.background_color = (0.9, 0.9, 0.9, 1)
        self.option_cls.color = (0, 0, 0, 1)  # Black text