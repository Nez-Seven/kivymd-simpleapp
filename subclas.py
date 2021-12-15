from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.toast import toast
from kivy.properties import ObjectProperty
from kivy.factory import Factory
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.gridlayout import GridLayout
from popups import popforerror
from popups import pop1
from popups import pop2
from popups import pop3
from popups import pop4
from popups import pop5
from popups import pop6
from popups import pop7
from popups import pop8
from popups import pop9
from popups import pop10
from popups import pop11
from popups import pop12
from popups import pop13
from popups import pop14
from popups import pop15
from popups import pop16
from popups import pop17
from popups import pop18
from popups import pop19
from popups import pop20
from kivy.uix.scrollview import ScrollView
import random
class MyGrid(MDFloatLayout):
    def __init__(self,**kwargs):
        super(MyGrid,self).__init__(**kwargs)
        self.size_hint = (1, 1)
        text1 = ObjectProperty(None)
        text2 = ObjectProperty(None)
        Exit1 = ObjectProperty()
    def btn1(self):
        v1 =  self.text1.text
        v2 = self.text2.text
        self.text1.text = ""
        self.text2.text = ""
        try:
            if len(v1) > 4 and len(v2) > 4:
                print("more than 100 is not allowed")
            elif v1 == "" and v2 == "":
                self.toast = toast("Both textfield is empty")
            elif v1 == "":
                self.toast=toast("text field1 empty")
            elif v2 == "":
                self.toast = toast("text field2 is empty")
            else:
                luckiness_of_user = random.randint(1, 10)
                number_of_good_deeds = int(v1)
                number_of_sin_deeds = int(v2)
                hell_calculator = luckiness_of_user * number_of_good_deeds / number_of_sin_deeds
                convert_hell_calculator = int(hell_calculator)
                print(convert_hell_calculator)
                if convert_hell_calculator <= 10:
                    p1 = pop1()
                elif convert_hell_calculator <= 20:
                    p2 = pop2()
                elif convert_hell_calculator <= 30:
                    p3 = pop3()
                elif convert_hell_calculator <= 40:
                    p3 = pop4()
                elif convert_hell_calculator <= 50:
                    p4 = pop5()
                elif convert_hell_calculator <=60:
                    p5 = pop5()
                elif convert_hell_calculator <=10:
                    p6= pop6()
                elif convert_hell_calculator <=20:
                    p7 = pop7()
                elif convert_hell_calculator <=30:
                    p8 = pop8()
                elif convert_hell_calculator <=40:
                    p9 = pop9()
                elif convert_hell_calculator <=50:
                    p10 = pop10()
                elif convert_hell_calculator <=60:
                    p11 = pop11()
                elif convert_hell_calculator <=10:
                    p12 = pop12()
                elif convert_hell_calculator <=20:
                    p13 = pop13()
                elif convert_hell_calculator <=30:
                    p14 = pop14()
                elif convert_hell_calculator <=40:
                    p15 = pop15()
                elif convert_hell_calculator <=50:
                    p16 = pop16()
                elif convert_hell_calculator <=60:
                    p17 = pop17()
                elif convert_hell_calculator <=70:
                    p18 = pop18()
                elif convert_hell_calculator <=80:
                    p19 = pop19()
                elif convert_hell_calculator <=90:
                    p20 = pop20()
                elif convert_hell_calculator <=100:
                    print("21")
                elif convert_hell_calculator not in range(0, 100):
                    print("you are lying and you are thrown out")            
        except ZeroDivisionError:
            #self.toast=toast("zero division error")
            error = popforerror()
class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()