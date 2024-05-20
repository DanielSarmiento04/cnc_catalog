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
    LightButton,
    LightSpinner
)
from .constants import (
    DIAMETERS,
    OPERATIONS,
    OPERATION_RANGE
)
from kivy.core.window import Window
from kivy.uix.spinner import Spinner
import pandas as pd

class HeadersContent(GridLayout):
    """  """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.cols = 4
        self.spacing = 10
        self.padding = 10
        
        self.padding = [10, 0 , 10, 0]
        self.spacing = 10
        


class CNCApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "CNC App"
        self.icon = "icon.png"
        self.data_frame_type_operation = None

    def build(self):
        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        with main_layout.canvas.before:
            Color(1, 1, 1, 1)  # White background
            self.rect = Rectangle(size=Window.size, pos=main_layout.pos)

        # Bind the size of the Rectangle to the window size
        Window.bind(size=self._update_rect, on_resize=self._update_rect)
        
        # Header layout
        main_layout.add_widget(
            LightLabel(
                text="Catálogo Kennametal",
                font_size=30,
                color=(0, 0, 0, 1),
                size_hint=(1, None),
                height=44
            )
        )
        
        main_layout.add_widget(
            LightLabel(
                text="Proceso de mecanizado: Fresado`",
                font_size=30,
                color=(0, 0, 0, 1),
                size_hint=(1, None),
                height=44
            )
        )

        headers_widget= HeadersContent(cols=3)

        spinner_block_option = BoxLayout(orientation='horizontal', size_hint=(1, None), height=44, spacing=10, padding=[10, 0, 10, 0])
        spinner_label_option = LightLabel(text="Operación:", size_hint=(None, 1), width=120)
        self.spinner_operation_options = LightSpinner(
            text='Seleccione operación',
            values=OPERATIONS,
            size_hint=(1, None),
            height=44,
        )
        self.spinner_operation_options.bind(text=self.select_operation)
        spinner_block_option.add_widget(spinner_label_option)
        spinner_block_option.add_widget(self.spinner_operation_options)
        
        headers_widget.add_widget(spinner_block_option)

        spinner_block_diameter = BoxLayout(orientation='horizontal', size_hint=(1, None), height=44, spacing=10, padding=[10, 0, 10, 0])
        spinner_label_diameter = LightLabel(text="Diámetros:", size_hint=(None, 1), width=120)
        self.spinner_diameter = LightSpinner(
            text='Seleccione diámetro',
            values=[],
            size_hint=(1, None),
            height=44,
        )
        self.spinner_diameter.bind(text=self.select_diameter)
        spinner_block_diameter.add_widget(spinner_label_diameter)
        spinner_block_diameter.add_widget(self.spinner_diameter)
        
        headers_widget.add_widget(spinner_block_diameter)

        spinner_block_range_operation = BoxLayout(orientation='horizontal', size_hint=(1, None), height=44, spacing=10, padding=[10, 0, 10, 0])
        spinner_label_range_operation = LightLabel(text="Rango de operación:", size_hint=(None, 1), width=120)
        self.spinner_range_operation = LightSpinner(
            text='Seleccione rango de operación',
            values=OPERATION_RANGE,
            size_hint=(1, None),
            height=44,
        )
        self.spinner_range_operation.bind(text=self.select_range_operation)
        spinner_block_range_operation.add_widget(spinner_label_range_operation)
        spinner_block_range_operation.add_widget(self.spinner_range_operation)
        
        headers_widget.add_widget(spinner_block_range_operation)

        
        main_layout.add_widget(headers_widget)
        return main_layout

    def _update_rect(self, *args):
        self.rect.size = Window.size
        self.rect.pos = (0, 0)

    def select_tool(self, tool):
        '''
            function to configure the spinner of the tool event
        '''
        self.label.text = f"Selected Tool: {tool}"
        self.main_button.text = tool

    def select_operation(self, spinner, text):
        '''
            function to configure the spinner of the operation event
        '''
        print(f"Selected operation: {text}")  # You can update this method to handle the selection

        self.data_frame_type_operation = pd.read_csv(
            f"./app/data/operation/{text.lower()}.csv"
        )
        self.spinner_diameter.values = self.data_frame_type_operation['D1'] \
                                        .unique() \
                                        .astype(str) \
                                        .tolist()

        # Apply light theme to new options
        self.spinner_diameter.option_cls.background_color = (0.9, 0.9, 0.9, 1)
        self.spinner_diameter.option_cls.color = (0, 0, 0, 1)  # Black text

    def select_diameter(self, spinner, text):
        '''
            function to configure the spinner of the diameter event
        '''
        print(f"Selected diameter: {text}")  # Handle diameter selection as needed

    def select_range_operation(self, spinner, text):
        '''
            function to configure the spinner of the range operation event
        '''
        print(f"Selected range operation: {text}")  # Handle range operation selection as needed