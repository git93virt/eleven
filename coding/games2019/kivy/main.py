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
from kivy.uix.relativelayout import RelativeLayout


class canvasex(Widget):
    pass


class canvasex1(Widget):
    pass


class canvasex2(Widget):
    pass


class canvasex3(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(0, 1, 0)
            Line(points=(100, 200, 500, 400), width=2)
            Color(0, 1, 1)
            Line(circle=(200, 300, 50), width=3)
            Color(.3, .7, .4)
            Line(rectangle=(20, 30, 50, 80), width=3)
            Rectangle(pos=(500, 200), width=(200, 300))

class canvasex4(BoxLayout):
    pass


class blockrect(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(0, 1, 0)
            # Line(points=(100, 200, 500, 400), width=2)
            # Color(0, 1, 1)
            # Line(circle=(200, 300, 50), width=3)
            # Color(.3, .7, .4)
            # Line(rectangle=(20, 30, 50, 80), width=3)
            self.rect = Rectangle(pos=(500, 200), width=(200, 300))

    def clickmoveright(self):
        print("clickedright")
        x, y = self.rect.pos
        w, h = self.rect.size
        increment = dp(10)
        diff = self.width-(x+w)
        if diff < increment:
            increment = diff

        x += increment
        self.rect.pos = (x, y)

    def clickmoveleft(self):
        print("clickedleft")
        x, y = self.rect.pos
        w, h = self.rect.size
        increment = dp(10)
        diff = self.width-(y-w)
        if diff < increment:
            increment = diff

        x -= increment
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


class stacklayoutex(StackLayout):
    pass


class sliderex(Slider):
    pass


class switchex(Switch):
    pass


class widgetex(GridLayout):

    mytest = StringProperty("0")
    count = 0
    count_enable = BooleanProperty(False)
    slidertext = StringProperty("50")

    def tooglefunction(self, widget):
        print("toogle")
        print(widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enable = False
        else:
            widget.text = "ON"
            self.count_enable = True
            self.disabled = False

    def onButtonClick(self):
        print(self.count)
        if self.count_enable:
            self.count += 1
            self.mytest = str(self.count)

    def onswitchactive(self, widget):
        print("switch:" + str(widget.active))

    def onslidervalue(self, widget):

        print("slider:" + str(int(widget.value)))
        self.slidertext = str(int(widget.value))


class Boxlayoutex(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     b1 = Button(text="hello")
    #     b2 = Button(text="newlayout")
    #     self.add_widget(b1)
    #     self.add_widget(b2)


class mainwidget(Widget):
    pass


class anchorlayoutex(AnchorLayout):
    pass


class gridlayoutex(GridLayout):
    pass


class lab(App):
    pass


lab().run()
