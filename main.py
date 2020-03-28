from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
import sys
import os

sys.path.append(os.path.dirname(__file__))

sys.path.append(os.path.join(os.path.dirname(__file__), "Main"))
print(sys.path)
import MainTutorial

sys.path.append(os.path.join(os.path.dirname(__file__), "MooseSystems"))
import MooseDecideScreen
MooseDecideScreen.importFiles()

sys.path.append(os.path.join(os.path.dirname(__file__), "Installation"))
import InstallationDecideScreen
InstallationDecideScreen.importFiles()

sys.path.append(os.path.join(os.path.dirname(__file__), "Recurring"))
import RecurringThemesScreen
RecurringThemesScreen.importFiles()

from kivy.uix.screenmanager import ScreenManager, Screen

class MainScreen(Screen):
    pass

class MainApp(App):
    pass

if __name__ == '__main__':
    MainApp().run()
