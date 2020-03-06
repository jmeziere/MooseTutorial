from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
import sys

sys.path.append('Main/')
import MainTutorial

sys.path.append('MooseSystems/')
import MooseDecideScreen
MooseDecideScreen.importFiles()

sys.path.append('Installation/')

from kivy.uix.screenmanager import ScreenManager, Screen

class MainScreen(Screen):
    pass

class MainApp(App):
    pass

if __name__ == '__main__':
    MainApp().run()
