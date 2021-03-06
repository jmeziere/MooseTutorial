from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import os

class InitScreen(Screen):
    pass

class AboutInl(Screen):
    pass

class AboutMoose(Screen):
    def getAboutMooseString(self):
        with open(os.path.join(os.path.dirname(__file__), "AboutMoose.txt"),'r') as file:
            data = file.read()
        return data

class AboutTutorial(Screen):
    def getAboutTutorialString(self):
        with open(os.path.join(os.path.dirname(__file__), "AboutTutorial.txt"),'r') as file:
            data = file.read()
        return data

Builder.load_string("""
<InitScreen>
    name: 'init_screen'
    StackLayout:
        orientation: 'rl-bt'
        Button:
            size_hint: None, None
            height: 50
            width: 100
            text: 'Next'
            on_release: App.get_running_app().root.ids.tutorial_manager.current = 'about_inl'
        Button:
            size_hint: None, None
            height: 50
            width: 100
            text: 'Previous'
            background_color: 0,0,0,1
    Label:
        text: 'Welcome To MOOSE!'
        font_size: 50

<AboutInl>
    name: 'about_inl'
    StackLayout:
        orientation: 'rl-bt'
        Button:
            size_hint: None, None
            height: 50
            width: 100
            text: 'Next'
            on_release: App.get_running_app().root.ids.tutorial_manager.current = 'about_moose'
        Button:
            size_hint: None, None
            height: 50
            width: 100
            text: 'Previous'
            on_release: App.get_running_app().root.ids.tutorial_manager.current = 'init_screen'
    Label:
        text: 'This page has nothing on it :('

<AboutMoose>
    name: 'about_moose'
    id: about_moose
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            Label:
                size_hint_y: None
                height: self.texture_size[1]
                text_size: self.width, None
                text: about_moose.getAboutMooseString()
        StackLayout:
            orientation: 'rl-bt'
            size_hint_y: None
            height: 50
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Next'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'about_tutorial'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Previous'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'about_inl'


<AboutTutorial>
    name: 'about_tutorial'
    id: about_tutorial
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            Label:
                size_hint_y: None
                height: self.texture_size[1]
                text_size: self.width, None
                text: about_tutorial.getAboutTutorialString()
        StackLayout:
            orientation: 'rl-bt'
            size_hint_y: None
            height: 50
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Next'
                background_color: 0,0,0,1
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Previous'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'about_moose'
""", filename = "MainTutorial.kv")
