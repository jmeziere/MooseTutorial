import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "Linux"))
import Mint18
import Mint19
import Ubuntu16_04
import Ubuntu18_04
import Fedora
from kivy.lang import Builder

Builder.load_string("""
<InstallationDecideScreen@Screen>
    name: 'installation_decide_screen'
    id: installation_decide_screen
    StackLayout:
        orientation: 'tb-lr'
        size_hint_x: None
        width: 100
        Label:
            bold: True
            underline: True
            #color: 1,0,0,0
            text: 'Linux'
            size_hint_y: None
            height: 30
            canvas.before:
                Color:
                    rgba: 1,0,0,1
                Rectangle:
                    pos: self.pos
                    size: self.size
        Button:
            id: Ubuntu18_04_button
            size_hint_y: None
            height: 30
            text: 'Ubuntu19'
            background_color: 0,0,0,1
            on_press: Ubuntu18_04_button.background_color = [1,1,1,1]
            on_release: App.get_running_app().root.ids.sub_sections.width = 0
            on_release: App.get_running_app().root.ids.installation_button.background_color = [0,0,0,1]
            on_release: Ubuntu18_04_button.background_color = [0,0,0,1]
            on_release: App.get_running_app().root.ids.tutorial_manager.current = 'Ubuntu18_04'
        Button:
            id: Ubuntu18_04_button2
            size_hint_y: None
            height: 30
            text: 'Ubuntu18.04'
            background_color: 0,0,0,1
            on_press: Ubuntu18_04_button2.background_color = [1,1,1,1]
            on_release: App.get_running_app().root.ids.sub_sections.width = 0
            on_release: App.get_running_app().root.ids.installation_button.background_color = [0,0,0,1]
            on_release: Ubuntu18_04_button2.background_color = [0,0,0,1]
            on_release: App.get_running_app().root.ids.tutorial_manager.current = 'Ubuntu18_04'
        Button:
            id: Ubuntu16_04_button
            size_hint_y: None
            height: 30
            text: 'Ubuntu16.04'
            background_color: 0,0,0,1
            on_press: Ubuntu16_04_button.background_color = [1,1,1,1]
            on_release: App.get_running_app().root.ids.sub_sections.width = 0
            on_release: App.get_running_app().root.ids.installation_button.background_color = [0,0,0,1]
            on_release: Ubuntu16_04_button.background_color = [0,0,0,1]
            on_release: App.get_running_app().root.ids.tutorial_manager.current = 'Ubuntu16_04'
        Button:
            id: Mint19_button
            size_hint_y: None
            height: 30
            text: 'Mint19'
            background_color: 0,0,0,1
            on_press: Mint19_button.background_color = [1,1,1,1]
            on_release: App.get_running_app().root.ids.sub_sections.width = 0
            on_release: App.get_running_app().root.ids.installation_button.background_color = [0,0,0,1]
            on_release: Mint19_button.background_color = [0,0,0,1]
            on_release: App.get_running_app().root.ids.tutorial_manager.current = 'Mint19'
        Button:
            id: Mint18_button
            size_hint_y: None
            height: 30
            text: 'Mint18'
            background_color: 0,0,0,1
            on_press: Mint18_button.background_color = [1,1,1,1]
            on_release: App.get_running_app().root.ids.sub_sections.width = 0
            on_release: App.get_running_app().root.ids.installation_button.background_color = [0,0,0,1]
            on_release: Mint18_button.background_color = [0,0,0,1]
            on_release: App.get_running_app().root.ids.tutorial_manager.current = 'Mint18'
        Button:
            id: Fedora_button
            size_hint_y: None
            height: 30
            text: 'Fedora'
            background_color: 0,0,0,1
            on_press: Fedora_button.background_color = [1,1,1,1]
            on_release: App.get_running_app().root.ids.sub_sections.width = 0
            on_release: App.get_running_app().root.ids.installation_button.background_color = [0,0,0,1]
            on_release: Fedora_button.background_color = [0,0,0,1]
            on_release: App.get_running_app().root.ids.tutorial_manager.current = 'Fedora'



        Label:
            bold: True
            underline: True
            #color: 1,0,0,0
            text: 'MacOS'
            size_hint_y: None
            height: 30
            canvas.before:
                Color:
                    rgba: 1,0,0,1
                Rectangle:
                    pos: self.pos
                    size: self.size


        Button:
            id: Catalina_button
            size_hint_y: None
            height: 30
            text: 'Catalina'
            background_color: 0,0,0,1
            on_press: Catalina_button.background_color = [1,1,1,1]
            on_release: App.get_running_app().root.ids.sub_sections.width = 0
            on_release: App.get_running_app().root.ids.installation_button.background_color = [0,0,0,1]
            on_release: Catalina_button.background_color = [0,0,0,1]
            on_release: App.get_running_app().root.ids.tutorial_manager.current = 'needs_work'

        Button:
            id: Mojave
            size_hint_y: None
            height: 30
            text: 'Mojave'
            background_color: 0,0,0,1
            on_press: Mojave_button.background_color = [1,1,1,1]
            on_release: App.get_running_app().root.ids.sub_sections.width = 0
            on_release: App.get_running_app().root.ids.installation_button.background_color = [0,0,0,1]
            on_release: Mojave_button.background_color = [0,0,0,1]
            on_release: App.get_running_app().root.ids.tutorial_manager.current = 'needs_work'

        Button:
            id: HighSierra
            size_hint_y: None
            height: 30
            text: 'High Sierra'
            background_color: 0,0,0,1
            on_press: HighSierra.background_color = [1,1,1,1]
            on_release: App.get_running_app().root.ids.sub_sections.width = 0
            on_release: App.get_running_app().root.ids.installation_button.background_color = [0,0,0,1]
            on_release: HighSierra_button.background_color = [0,0,0,1]
            on_release: App.get_running_app().root.ids.tutorial_manager.current = 'needs_work'
""", filename = "InstallationDecideScreen.kv")
