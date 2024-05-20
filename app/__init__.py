from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics import Color, Rectangle
from .components import (
    LightLabel,
    LightButton
)
from kivy.core.window import Window


class Columns(GridLayout):
    """  """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.cols = 4
        self.spacing = 10
        self.padding = 10
        self.bind(minimum_height=self.minimum_height)
        self.bind(minimum_width=self.minimum_width)


class CNCApp(App):

    def build(self):
        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        with main_layout.canvas.before:
            Color(1, 1, 1, 1)  # White background
            self.rect = Rectangle(size=Window.size)


        # Header layout
        header_layout = GridLayout(cols=4, size_hint_y=None, height=44)

        headers = ["Operación", "Diámetro Herramienta", "Ángulo", "Número de insertos"]
        for header in headers:
            header_label = LightLabel(text=header, bold=True)
            header_layout.add_widget(header_label)

        main_layout.add_widget(header_layout)

        # Label
        self.label = LightLabel(text="Select a CNC Tool", font_size='20sp')
        main_layout.add_widget(self.label)

        # Dropdown for tool selection
        self.dropdown = DropDown()

        tools = ['Drill', 'End Mill', 'Lathe', 'Grinder']
        for tool in tools:
            btn = LightButton(text=tool, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
            self.dropdown.add_widget(btn)

        # Main button that opens the dropdown
        self.main_button = LightButton(text='Choose Tool', size_hint=(1, None), height=44)
        self.main_button.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: self.select_tool(x))

        main_layout.add_widget(self.main_button)

        return main_layout

    def select_tool(self, tool):
        self.label.text = f"Selected Tool: {tool}"
        self.main_button.text = tool