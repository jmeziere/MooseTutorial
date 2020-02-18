from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from FirstScreen import FirstScreen
from SecondScreen import SecondScreen

from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

import time
import random

Builder.load_file('FirstScreen.kv')
Builder.load_file('SecondScreen.kv')

class MainApp(App):
    pass

if __name__ == '__main__':
    MainApp().run()
