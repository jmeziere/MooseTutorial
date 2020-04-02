from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
import commonMethods
from kivy.lang import Builder
import os
import _thread

class AuxiliaryVariablesOverview(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = commonMethods.niceLayout(width,'auxiliaryVariablesOverview', os.path.dirname(__file__))
        for label in new_labels:
            b_layout.add_widget(label)
        return height

class AuxiliaryVariablesMemberVariables(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = commonMethods.niceLayout(width,'auxiliaryVariablesMemberVariables', os.path.dirname(__file__))
        for label in new_labels:
            b_layout.add_widget(label)
        return height

class AuxiliaryVariablesMemberFunctions(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = commonMethods.niceLayout(width,'auxiliaryVariablesMemberFunction', os.path.dirname(__file__))
        for label in new_labels:
            b_layout.add_widget(label)
        return height

class AuxiliaryVariablesExample(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = commonMethods.niceLayout(width,'auxiliaryVariablesExample', os.path.dirname(__file__))
        for label in new_labels:
            b_layout.add_widget(label)
        return height

    def runSimulation(self):
        _thread.start_new_thread(commonMethods.runSimulation,('projects/moose/tutorials/darcy_thermo_mech/step01_diffusion/problems/step1.i',))

class AuxiliaryVariablesProblem(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = commonMethods.niceLayout(width,'auxiliaryVariablesProblem', os.path.dirname(__file__))
        for label in new_labels:
            b_layout.add_widget(label)
        return height

class AuxiliaryVariablesSolution(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = commonMethods.niceLayout(width,'auxiliaryVariablesSolution', os.path.dirname(__file__))
        for label in new_labels:
            b_layout.add_widget(label)
        return height

Builder.load_string("""
<AuxiliaryVariablesOverview>
    name: 'auxiliary_variables_overview'
    id: auxiliary_variables_overview
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                id: tester
                orientation: 'vertical'
                size_hint_y: None
                height: auxiliary_variables_overview.addText(root.width)
        StackLayout:
            orientation: 'rl-bt'
            size_hint_y: None
            height: 50
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Next'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'auxiliary_variables_member_variables'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Previous'
                background_color: 0,0,0,1

<AuxiliaryVariablesMemberVariables>
    name: 'auxiliary_variables_member_variables'
    id: auxiliary_variables_member_variables
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                id: tester
                orientation: 'vertical'
                size_hint_y: None
                height: auxiliary_variables_member_variables.addText(root.width)
        StackLayout:
            orientation: 'rl-bt'
            size_hint_y: None
            height: 50
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Next'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'auxiliary_variables_member_functions'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Previous'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'auxiliary_variables_overview'

<AuxiliaryVariablesMemberFunctions>
    name: 'auxiliary_variables_member_functions'
    id: auxiliary_variables_member_functions
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                id: tester
                orientation: 'vertical'
                size_hint_y: None
                height: auxiliary_variables_member_functions.addText(root.width)
        StackLayout:
            orientation: 'rl-bt'
            size_hint_y: None
            height: 50
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Next'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'auxiliary_variables_example'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Previous'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'auxiliary_variables_member_variables'

<AuxiliaryVariablesExample>
    name: 'auxiliary_variables_example'
    id: auxiliary_variables_example
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                id: tester
                orientation: 'vertical'
                size_hint_y: None
                height: auxiliary_variables_example.addText(root.width)
        StackLayout:
            orientation: 'rl-bt'
            size_hint_y: None
            height: 50
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Next'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'auxiliary_variables_problem'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Previous'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'auxiliary_variables_member_functions'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Run\\nSimulation'
                halign: 'center'
                on_release: auxiliary_variables_example.runSimulation()

<AuxiliaryVariablesProblem>
    name: 'auxiliary_variables_problem'
    id: auxiliary_variables_problem
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                id: tester
                orientation: 'vertical'
                size_hint_y: None
                height: auxiliary_variables_problem.addText(root.width)
        StackLayout:
            orientation: 'rl-bt'
            size_hint_y: None
            height: 50
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Next'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'auxiliary_variables_solution'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Previous'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'auxiliary_variables_example'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Run\\nSimulation'
                halign: 'center'

<AuxiliaryVariablesSolution>
    name: 'auxiliary_variables_solution'
    id: auxiliary_variables_solution
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                id: tester
                orientation: 'vertical'
                size_hint_y: None
                height: auxiliary_variables_solution.addText(root.width)
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
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'auxiliary_variables_problem'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Run\\nSimulation'
                halign: 'center'
""", filename = "auxiliaryVariables.kv")
