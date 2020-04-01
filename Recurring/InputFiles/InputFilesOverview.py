from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
import commonMethods
from kivy.lang import Builder
import os

class InputFilesOverview(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = commonMethods.niceLayout(width,'InputFilesOverview', os.path.dirname(__file__))
        for label in new_labels:
            b_layout.add_widget(label)
        return height

class InputFilesExample(Screen):
    pass
"""    def getKernelsOverviewString(self):
        with open('InputFilesExample.txt') as file:
            data = file.read()
        return data"""

class InputFilesProblem(Screen):
    pass
    """def getKernelsOverviewString(self):
        with open('InputFilesProblem.txt') as file:
            data = file.read()
        return data"""

class InputFilesSolution(Screen):
    pass
    """def getKernelsOverviewString(self):
        with open('InputFilesSolution.txt') as file:
            data = file.read()
        return data """

Builder.load_string("""
<InputFilesOverview@Screen>
    name: 'input_files_overview'
    id: input_files_overview
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                id: tester
                orientation: 'vertical'
                size_hint_y: None
                height: input_files_overview.addText(root.width)
        StackLayout:
            orientation: 'rl-bt'
            size_hint_y: None
            height: 50
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Next'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'input_files_example'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Previous'
                background_color: 0,0,0,1

<InputFilesExample>
    name: 'input_files_example'
    id: kernels_example
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            Label:
                size_hint_y: None
                height: self.texture_size[1]
                text_size: self.width, None
                text: "Example"
        StackLayout:
            orientation: 'rl-bt'
            size_hint_y: None
            height: 50
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Next'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'input_files_problem'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Previous'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'input_files_overview'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Run\\nSimulation'
                halign: 'center'

<InputFilesProblem>
    name: 'input_files_problem'
    id: kernels_problem
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            Label:
                size_hint_y: None
                height: self.texture_size[1]
                text_size: self.width, None
                text: "Problem"
        StackLayout:
            orientation: 'rl-bt'
            size_hint_y: None
            height: 50
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Next'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'input_files_solution'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Previous'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'input_files_example'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Run\\nSimulation'
                halign: 'center'

<InputFilesSolution>
    name: 'input_files_solution'
    id: kernels_solution
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            Label:
                size_hint_y: None
                height: self.texture_size[1]
                text_size: self.width, None
                text: "Solution"
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
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'input_files_problem'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Run\\nSimulation'
                halign: 'center'
""", filename = "InputFilesOverview.kv")
