from kivy.uix.label import Label

class LightLabel(Label):
    """Label with light theme"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = (0, 0, 0, 1)  # Black text
