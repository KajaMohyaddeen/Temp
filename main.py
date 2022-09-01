import random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.animation import Animation
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager,Screen,WipeTransition

class MyPopup(Popup):  # 
    # window refers Popupwindow class reference 
       
    window_ref = None

    def popup_open(self,window):
        self.window_ref = window
        
        self.window_ref.popob.open()
       
    def popup_dismiss(self,status):
        if status:
            self.window_ref.refresh()
            self.dismiss()
        else: 
            self.dismiss()
            
class InfoWindow(Screen):
    pass
            
# Home Window            
class FirstWindow(Screen):    
    
    count = 0
    sound = None
           
    def refresh(self):
        ob = self.manager.get_screen("secondwindow")
        ob.bot_points =0;
        ob.user_points = 0;
        ob.user_choice='user'
        ob.bot_choice='bot'
        
 
    def Toggle(self):
        ob3 = self.manager.get_screen('thirdwindow')
        self.count += 1 
                       
        if self.count%2 ==1:      
            ob3.music_play()
        else:            
            ob3.music_stop()
             
# Game Window
class SecondWindow(Screen):
    angle = NumericProperty(0)
    sound = SoundLoader.load('Music/buttonclick.mp3')
    
    def call_back(self,ob):
        
        thrd = self.manager.get_screen('thirdwindow')
    
        self.sound.volume = thrd.ids.vol_slider.value/4
        self.sound.play()
        
        choices = ['ROCK','PAPER','SCISSORS']      
        self.user_choice = ob.text      
        self.bot_choice = random.choice(choices)
                 
        points = ['ROCKPAPER','PAPERSCISSORS','SCISSORSROCK']
               
        if self.bot_choice + self.user_choice in points:     
            self.user_points += 1    
        elif self.bot_choice ==  self.user_choice:
            pass
        else:
            self.bot_points += 1
                        
        if self.user_points == 10:
            frth = self.manager.get_screen('fourthwindow')
            frth.result_func('USER')
            App.get_running_app().root.current = 'fourthwindow'
        elif self.bot_points==10:
            frth = self.manager.get_screen('fourthwindow')
            frth.result_func('BOT')
            App.get_running_app().root.current = 'fourthwindow'
            
    def Exit(self):
        App.get_running_app().stop()
   
    
    def Animate_Rotate(self,obj):
        anim = Animation(angle=360,duration=2)
        anim.start(obj)


#Settings Window
class ThirdWindow(Screen): 
             
    sound = SoundLoader.load('Music/music.mp3')
    def music_play(self):
        self.sound.play()
        
    def music_stop(self):
        self.sound.stop()
        
    def volume(self,*args):      
        self.sound.volume = args[1]
          
    def brightness(self,*args):
        App.get_running_app().root.opacity = args[1]
        
class FourthWindow(Screen):

   def result_func(self,winner):
        self.result = winner
        
class Progress(Widget):
        pass
        
class GameWindow(ScreenManager):
    pass  
   
class MyGameApp(App):
          
    def build(self):        
        return GameWindow()

if __name__ == '__main__':  

    MyGameApp().run()
