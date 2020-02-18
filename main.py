from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from InstallationScreen import InstallationScreen
from InputFileScreen import InputFileScreen
from MathTutorialScreen import MathTutorialScreen
from MooseCodingScreen import MooseCodingScreen


from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

import time
import random

Builder.load_file('InstallationScreen.kv')
Builder.load_file('MathTutorialScreen.kv')
Builder.load_file('InputFileScreen.kv')
Builder.load_file('MooseCodingScreen.kv')

class MainScreen(Screen):
    pass

class MainApp(App):
    pass

if __name__ == '__main__':
    MainApp().run()
