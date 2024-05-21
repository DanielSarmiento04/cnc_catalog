from kivy.uix.spinner import Spinner
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button

class LightSpinnerOption(Button):
    """Custom option class for LightSpinner"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (0.9, 0.9, 0.9, 1)  # Light gray background
        self.color = (0, 0, 0, 1)  # Black text

class LightSpinnerDropDown(DropDown):
    """Dropdown class for LightSpinner"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.option_cls = LightSpinnerOption  # Use custom option class

class LightSpinner(Spinner):
    """Spinner with light theme"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (0.9, 0.9, 0.9, 1)  # Light gray background
        self.color = (0, 0, 0, 1)  # Black text
        self.dropdown_cls = LightSpinnerDropDown  # Use custom dropdown class

