from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.switch import Switch
from kivy.uix.slider import Slider
from kivy.graphics.vertex_instructions import Line, Rectangle
from kivy.graphics.context_instructions import Color
from kivy.metrics import dp

class canvasex4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(0, 1, 0)
            Line(points=(100, 200, 500, 400), width=2)
            Color(0, 1, 1)
            Line(circle=(200, 300, 50), width=3)
            Color(.3, .7, .4)
            Line(rectangle=(20, 30, 50, 80), width=3)
            self.rect = Rectangle(pos=(500, 200), width=(200, 300))

    def clickmoveright(self):
        print("clickedright")
        x, y = self.rect.pos
        x += dp(10)
        self.rect.pos = (x, y)

    def clickmoveleft(self):
        print("clickedleft")
        x, y = self.rect.pos
        x -= dp(10)
        self.rect.pos = (x, y)

    def clickmoveup(self):
        print("clickedup")
        x, y = self.rect.pos
        y += dp(10)
        self.rect.pos = (x, y)

    def clickmovedown(self):
        print("clickeddown")
        x, y = self.rect.pos
        y -= dp(10)
        self.rect.pos = (x, y)


class move(App):    #to create a GUI window
    pass


move().run()    # to open a GUI window
