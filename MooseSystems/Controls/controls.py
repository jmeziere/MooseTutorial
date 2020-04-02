from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
import commonMethods
from kivy.lang import Builder
import os
import _thread

class ControlsOverview(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = commonMethods.niceLayout(width,'controlsOverview', os.path.dirname(__file__))
        for label in new_labels:
            b_layout.add_widget(label)
        return height

class ControlsMemberVariables(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = commonMethods.niceLayout(width,'controlsMemberVariables', os.path.dirname(__file__))
        for label in new_labels:
            b_layout.add_widget(label)
        return height

class ControlsMemberFunctions(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = commonMethods.niceLayout(width,'controlsMemberFunction', os.path.dirname(__file__))
        for label in new_labels:
            b_layout.add_widget(label)
        return height

class ControlsExample(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = commonMethods.niceLayout(width,'controlsExample', os.path.dirname(__file__))
        for label in new_labels:
            b_layout.add_widget(label)
        return height

    def runSimulation(self):
        _thread.start_new_thread(commonMethods.runSimulation,('projects/moose/tutorials/darcy_thermo_mech/step01_diffusion/problems/step1.i',))

class ControlsProblem(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = commonMethods.niceLayout(width,'controlsProblem', os.path.dirname(__file__))
        for label in new_labels:
            b_layout.add_widget(label)
        return height

class ControlsSolution(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = commonMethods.niceLayout(width,'controlsSolution', os.path.dirname(__file__))
        for label in new_labels:
            b_layout.add_widget(label)
        return height

Builder.load_string("""
<ControlsOverview>
    name: 'controls_overview'
    id: controls_overview
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                id: tester
                orientation: 'vertical'
                size_hint_y: None
                height: controls_overview.addText(root.width)
        StackLayout:
            orientation: 'rl-bt'
            size_hint_y: None
            height: 50
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Next'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'controls_member_variables'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Previous'
                background_color: 0,0,0,1

<ControlsMemberVariables>
    name: 'controls_member_variables'
    id: controls_member_variables
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                id: tester
                orientation: 'vertical'
                size_hint_y: None
                height: controls_member_variables.addText(root.width)
        StackLayout:
            orientation: 'rl-bt'
            size_hint_y: None
            height: 50
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Next'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'controls_member_functions'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Previous'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'controls_overview'

<ControlsMemberFunctions>
    name: 'controls_member_functions'
    id: controls_member_functions
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                id: tester
                orientation: 'vertical'
                size_hint_y: None
                height: controls_member_functions.addText(root.width)
        StackLayout:
            orientation: 'rl-bt'
            size_hint_y: None
            height: 50
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Next'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'controls_example'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Previous'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'controls_member_variables'

<ControlsExample>
    name: 'controls_example'
    id: controls_example
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                id: tester
                orientation: 'vertical'
                size_hint_y: None
                height: controls_example.addText(root.width)
        StackLayout:
            orientation: 'rl-bt'
            size_hint_y: None
            height: 50
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Next'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'controls_problem'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Previous'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'controls_member_functions'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Run\\nSimulation'
                halign: 'center'
                on_release: controls_example.runSimulation()

<ControlsProblem>
    name: 'controls_problem'
    id: controls_problem
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                id: tester
                orientation: 'vertical'
                size_hint_y: None
                height: controls_problem.addText(root.width)
        StackLayout:
            orientation: 'rl-bt'
            size_hint_y: None
            height: 50
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Next'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'controls_solution'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Previous'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'controls_example'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Run\\nSimulation'
                halign: 'center'

<ControlsSolution>
    name: 'controls_solution'
    id: controls_solution
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                id: tester
                orientation: 'vertical'
                size_hint_y: None
                height: controls_solution.addText(root.width)
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
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'controls_problem'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Run\\nSimulation'
                halign: 'center'
""", filename = "controls.kv")
