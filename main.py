from kivymd.app import MDApp
from kivy.properties import ObjectProperty
from subclas import MyGrid
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
from kivy.lang import Builder


class paroic(MDApp):
    def build(self):
        # Window.keyboard_anim_args={'d':0.2,'t':'in_out_expo'}
        Window.softinput_mode = 'below_target'
        self.theme_cls.hue = "700"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        main_layout = MyGrid()
        return main_layout


if __name__ == '__main__':
    app = paroic()
    app.run()
