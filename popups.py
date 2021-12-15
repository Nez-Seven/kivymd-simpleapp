from kivy.uix.popup import Popup
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
class PopExitcustumbtn1(Button): # custum button2
    def __init__(self,**kwargs):
        super(PopExitcustumbtn1,self).__init__(**kwargs)
        self.text="-----close-----"
        self.color=(14/255,209/255,69/255,1)
        self.pos_hint={'center_x':0.5,'center_y':0.5}
        self.size_hint=(0.8,0.15)
        self.background_color=(14/255,209/255,69/255,0)
        self.padding_x = 40
class pop1(Popup): # custum popup0-2
    def __init__(self,**kwargs):
        super(pop1,self).__init__(**kwargs)
        self.l=MDBoxLayout(orientation='vertical')
        self.i=Image(source='h1.png')
        self.closepopbtn=PopExitcustumbtn1()
        self.pop=Popup(title='1',content=self.l,size_hint=(0.5,0.5),pos_hint={'center_x':0.5,'center_y':0.5},background='o.png',title_color=(14/255,209/255,69/255,1),auto_dismiss=False)
        self.l.add_widget(self.i)
        self.font_size=15
        self.l.add_widget(self.closepopbtn)
        self.pop.open()
        self.closepopbtn.bind(on_press=self.pop.dismiss)
class pop2(Popup): # custum popup0-2
    def __init__(self,**kwargs):
        super(pop2,self).__init__(**kwargs)
        self.l=MDBoxLayout(orientation='vertical')
        self.i=Image(source='h2.png')
        self.closepopbtn=PopExitcustumbtn1()
        self.pop=Popup(title='2',content=self.l,size_hint=(0.5,0.5),pos_hint={'center_x':0.5,'center_y':0.5},background='o.png',title_color=(14/255,209/255,69/255,1),auto_dismiss=False)
        self.l.add_widget(self.i)
        self.font_size=15
        self.l.add_widget(self.closepopbtn)
        self.pop.open()
        self.closepopbtn.bind(on_press=self.pop.dismiss)
class pop3(Popup): # custum popup0-2
    def __init__(self,**kwargs):
        super(pop3,self).__init__(**kwargs)
        self.l=MDBoxLayout(orientation='vertical')
        self.i=Image(source='h3.png')
        self.closepopbtn=PopExitcustumbtn1()
        self.pop=Popup(title='3',content=self.l,size_hint=(0.5,0.5),pos_hint={'center_x':0.5,'center_y':0.5},background='o.png',title_color=(14/255,209/255,69/255,1),auto_dismiss=False)
        self.l.add_widget(self.i)
        self.font_size=15
        self.l.add_widget(self.closepopbtn)
        self.pop.open()
        self.closepopbtn.bind(on_press=self.pop.dismiss)

class pop4(Popup): # custum popup0-2
    def __init__(self,**kwargs):
        super(pop4,self).__init__(**kwargs)
        self.l=MDBoxLayout(orientation='vertical')
        self.i=Image(source='h4.png')
        self.closepopbtn=PopExitcustumbtn1()
        self.pop=Popup(title='4',content=self.l,size_hint=(0.5,0.5),pos_hint={'center_x':0.5,'center_y':0.5},background='o.png',title_color=(14/255,209/255,69/255,1),auto_dismiss=False)
        self.l.add_widget(self.i)
        self.font_size=15
        self.l.add_widget(self.closepopbtn)
        self.pop.open()
        self.closepopbtn.bind(on_press=self.pop.dismiss)
class pop5(Popup): # custum popup0-2
    def __init__(self,**kwargs):
        super(pop5,self).__init__(**kwargs)
        self.l=MDBoxLayout(orientation='vertical')
        self.i=Image(source='h5.png')
        self.closepopbtn=PopExitcustumbtn1()
        self.pop=Popup(title='5',content=self.l,size_hint=(0.5,0.5),pos_hint={'center_x':0.5,'center_y':0.5},background='o.png',title_color=(14/255,209/255,69/255,1),auto_dismiss=False)
        self.l.add_widget(self.i)
        self.font_size=15
        self.l.add_widget(self.closepopbtn)
        self.pop.open()
        self.closepopbtn.bind(on_press=self.pop.dismiss)

class pop6(Popup): # custum popup0-2
    def __init__(self,**kwargs):
        super(pop6,self).__init__(**kwargs)
        self.l=MDBoxLayout(orientation='vertical')
        self.i=Image(source='h6.png')
        self.closepopbtn=PopExitcustumbtn1()
        self.pop=Popup(title='6',content=self.l,size_hint=(0.5,0.5),pos_hint={'center_x':0.5,'center_y':0.5},background='o.png',title_color=(14/255,209/255,69/255,1),auto_dismiss=False)
        self.l.add_widget(self.i)
        self.font_size=15
        self.l.add_widget(self.closepopbtn)
        self.pop.open()
        self.closepopbtn.bind(on_press=self.pop.dismiss)
class pop7(Popup): # custum popup0-2
    def __init__(self,**kwargs):
        super(pop7,self).__init__(**kwargs)
        self.l=MDBoxLayout(orientation='vertical')
        self.i=Image(source='h7.png')
        self.closepopbtn=PopExitcustumbtn1()
        self.pop=Popup(title='7',content=self.l,size_hint=(0.5,0.5),pos_hint={'center_x':0.5,'center_y':0.5},background='o.png',title_color=(14/255,209/255,69/255,1),auto_dismiss=False)
        self.l.add_widget(self.i)
        self.font_size=15
        self.l.add_widget(self.closepopbtn)
        self.pop.open()
        self.closepopbtn.bind(on_press=self.pop.dismiss)
class pop8(Popup): # custum popup0-2
    def __init__(self,**kwargs):
        super(pop8,self).__init__(**kwargs)
        self.l=MDBoxLayout(orientation='vertical')
        self.i=Image(source='h8.png')
        self.closepopbtn=PopExitcustumbtn1()
        self.pop=Popup(title='8',content=self.l,size_hint=(0.5,0.5),pos_hint={'center_x':0.5,'center_y':0.5},background='o.png',title_color=(14/255,209/255,69/255,1),auto_dismiss=False)
        self.l.add_widget(self.i)
        self.font_size=15
        self.l.add_widget(self.closepopbtn)
        self.pop.open()
        self.closepopbtn.bind(on_press=self.pop.dismiss)

class pop9(Popup): # custum popup0-2
    def __init__(self,**kwargs):
        super(pop9,self).__init__(**kwargs)
        self.l=MDBoxLayout(orientation='vertical')
        self.i=Image(source='h9.png')
        self.closepopbtn=PopExitcustumbtn1()
        self.pop=Popup(title='9',content=self.l,size_hint=(0.5,0.5),pos_hint={'center_x':0.5,'center_y':0.5},background='o.png',title_color=(14/255,209/255,69/255,1),auto_dismiss=False)
        self.l.add_widget(self.i)
        self.font_size=15
        self.l.add_widget(self.closepopbtn)
        self.pop.open()
        self.closepopbtn.bind(on_press=self.pop.dismiss)
class pop10(Popup): # custum popup0-2
    def __init__(self,**kwargs):
        super(pop10,self).__init__(**kwargs)
        self.l=MDBoxLayout(orientation='vertical')
        self.i=Image(source='h10.png')
        self.closepopbtn=PopExitcustumbtn1()
        self.pop=Popup(title='10',content=self.l,size_hint=(0.5,0.5),pos_hint={'center_x':0.5,'center_y':0.5},background='o.png',title_color=(14/255,209/255,69/255,1),auto_dismiss=False)
        self.l.add_widget(self.i)
        self.font_size=15
        self.l.add_widget(self.closepopbtn)
        self.pop.open()
        self.closepopbtn.bind(on_press=self.pop.dismiss)

class pop11(Popup): # custum popup0-2
    def __init__(self,**kwargs):
        super(pop11,self).__init__(**kwargs)
        self.l=MDBoxLayout(orientation='vertical')
        self.i=Image(source='h11.png')
        self.closepopbtn=PopExitcustumbtn1()
        self.pop=Popup(title='11',content=self.l,size_hint=(0.5,0.5),pos_hint={'center_x':0.5,'center_y':0.5},background='o.png',title_color=(14/255,209/255,69/255,1),auto_dismiss=False)
        self.l.add_widget(self.i)
        self.font_size=15
        self.l.add_widget(self.closepopbtn)
        self.pop.open()
        self.closepopbtn.bind(on_press=self.pop.dismiss)

class pop12(Popup): # custum popup0-2
    def __init__(self,**kwargs):
        super(pop12,self).__init__(**kwargs)
        self.l=MDBoxLayout(orientation='vertical')
        self.i=Image(source='h12.png')
        self.closepopbtn=PopExitcustumbtn1()
        self.pop=Popup(title='12',content=self.l,size_hint=(0.5,0.5),pos_hint={'center_x':0.5,'center_y':0.5},background='o.png',title_color=(14/255,209/255,69/255,1),auto_dismiss=False)
        self.l.add_widget(self.i)
        self.font_size=15
        self.l.add_widget(self.closepopbtn)
        self.pop.open()
        self.closepopbtn.bind(on_press=self.pop.dismiss)


class pop13(Popup): # custum popup0-2
    def __init__(self,**kwargs):
        super(pop13,self).__init__(**kwargs)
        self.l=MDBoxLayout(orientation='vertical')
        self.i=Image(source='h13.png')
        self.closepopbtn=PopExitcustumbtn1()
        self.pop=Popup(title='13',content=self.l,size_hint=(0.5,0.5),pos_hint={'center_x':0.5,'center_y':0.5},background='o.png',title_color=(14/255,209/255,69/255,1),auto_dismiss=False)
        self.l.add_widget(self.i)
        self.font_size=15
        self.l.add_widget(self.closepopbtn)
        self.pop.open()
        self.closepopbtn.bind(on_press=self.pop.dismiss)

class pop14(Popup): # custum popup0-2
    def __init__(self,**kwargs):
        super(pop14,self).__init__(**kwargs)
        self.l=MDBoxLayout(orientation='vertical')
        self.i=Image(source='h14.png')
        self.closepopbtn=PopExitcustumbtn1()
        self.pop=Popup(title='14',content=self.l,size_hint=(0.5,0.5),pos_hint={'center_x':0.5,'center_y':0.5},background='o.png',title_color=(14/255,209/255,69/255,1),auto_dismiss=False)
        self.l.add_widget(self.i)
        self.font_size=15
        self.l.add_widget(self.closepopbtn)
        self.pop.open()
        self.closepopbtn.bind(on_press=self.pop.dismiss)
class pop15(Popup): # custum popup0-2
    def __init__(self,**kwargs):
        super(pop15,self).__init__(**kwargs)
        self.l=MDBoxLayout(orientation='vertical')
        self.i=Image(source='h15.png')
        self.closepopbtn=PopExitcustumbtn1()
        self.pop=Popup(title='15',content=self.l,size_hint=(0.5,0.5),pos_hint={'center_x':0.5,'center_y':0.5},background='o.png',title_color=(14/255,209/255,69/255,1),auto_dismiss=False)
        self.l.add_widget(self.i)
        self.font_size=15
        self.l.add_widget(self.closepopbtn)
        self.pop.open()
        self.closepopbtn.bind(on_press=self.pop.dismiss)
class pop16(Popup): # custum popup0-2
    def __init__(self,**kwargs):
        super(pop16,self).__init__(**kwargs)
        self.l=MDBoxLayout(orientation='vertical')
        self.i=Image(source='h16.png')
        self.closepopbtn=PopExitcustumbtn1()
        self.pop=Popup(title='16',content=self.l,size_hint=(0.5,0.5),pos_hint={'center_x':0.5,'center_y':0.5},background='o.png',title_color=(14/255,209/255,69/255,1),auto_dismiss=False)
        self.l.add_widget(self.i)
        self.font_size=15
        self.l.add_widget(self.closepopbtn)
        self.pop.open()
        self.closepopbtn.bind(on_press=self.pop.dismiss)
class pop17(Popup): # custum popup0-2
    def __init__(self,**kwargs):
        super(pop17,self).__init__(**kwargs)
        self.l=MDBoxLayout(orientation='vertical')
        self.i=Image(source='h17.png')
        self.closepopbtn=PopExitcustumbtn1()
        self.pop=Popup(title='17',content=self.l,size_hint=(0.5,0.5),pos_hint={'center_x':0.5,'center_y':0.5},background='o.png',title_color=(14/255,209/255,69/255,1),auto_dismiss=False)
        self.l.add_widget(self.i)
        self.font_size=15
        self.l.add_widget(self.closepopbtn)
        self.pop.open()
        self.closepopbtn.bind(on_press=self.pop.dismiss)
class pop18(Popup): # custum popup0-2
    def __init__(self,**kwargs):
        super(pop18,self).__init__(**kwargs)
        self.l=MDBoxLayout(orientation='vertical')
        self.i=Image(source='h18.png')
        self.closepopbtn=PopExitcustumbtn1()
        self.pop=Popup(title='18',content=self.l,size_hint=(0.5,0.5),pos_hint={'center_x':0.5,'center_y':0.5},background='o.png',title_color=(14/255,209/255,69/255,1),auto_dismiss=False)
        self.l.add_widget(self.i)
        self.font_size=15
        self.l.add_widget(self.closepopbtn)
        self.pop.open()
        self.closepopbtn.bind(on_press=self.pop.dismiss)
class pop19(Popup): # custum popup0-2
    def __init__(self,**kwargs):
        super(pop19,self).__init__(**kwargs)
        self.l=MDBoxLayout(orientation='vertical')
        self.i=Image(source='h19.png')
        self.closepopbtn=PopExitcustumbtn1()
        self.pop=Popup(title='19',content=self.l,size_hint=(0.5,0.5),pos_hint={'center_x':0.5,'center_y':0.5},background='o.png',title_color=(14/255,209/255,69/255,1),auto_dismiss=False)
        self.l.add_widget(self.i)
        self.font_size=15
        self.l.add_widget(self.closepopbtn)
        self.pop.open()
        self.closepopbtn.bind(on_press=self.pop.dismiss)
class pop20(Popup): # custum popup0-2
    def __init__(self,**kwargs):
        super(pop20,self).__init__(**kwargs)
        self.l=MDBoxLayout(orientation='vertical')
        self.i=Image(source='h20.png')
        self.closepopbtn=PopExitcustumbtn1()
        self.pop=Popup(title='20',content=self.l,size_hint=(0.5,0.5),pos_hint={'center_x':0.5,'center_y':0.5},background='o.png',title_color=(14/255,209/255,69/255,1),auto_dismiss=False)
        self.l.add_widget(self.i)
        self.font_size=15
        self.l.add_widget(self.closepopbtn)
        self.pop.open()
        self.closepopbtn.bind(on_press=self.pop.dismiss)
class popforerror(Popup): # zero divison error
    def __init__(self,**kwargs):
        super(popforerror,self).__init__(**kwargs)
        self.l=MDBoxLayout(orientation='vertical')
        self.i=Image(source='zero.png')
        self.closepopbtn=PopExitcustumbtn1()
        self.pop=Popup(title='15',content=self.l,size_hint=(0.5,0.5),pos_hint={'center_x':0.5,'center_y':0.5},background='o.png',title_color=(14/255,209/255,69/255,1),auto_dismiss=False)
        self.l.add_widget(self.i)
        self.font_size=15
        self.l.add_widget(self.closepopbtn)
        self.pop.open()
        self.closepopbtn.bind(on_press=self.pop.dismiss)
