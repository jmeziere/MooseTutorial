from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
import commonMethods
from kivy.lang import Builder
import os
import _thread

class AuxilaryVariablesOverview(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = commonMethods.niceLayout(width,'auxilaryVariablesOverview', os.path.dirname(__file__))
        for label in new_labels:
            b_layout.add_widget(label)
        return height

class AuxilaryVariablesMemberVariables(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = commonMethods.niceLayout(width,'auxilaryVariablesMemberVariables', os.path.dirname(__file__))
        for label in new_labels:
            b_layout.add_widget(label)
        return height

class AuxilaryVariablesMemberFunctions(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = commonMethods.niceLayout(width,'auxilaryVariablesMemberFunction', os.path.dirname(__file__))
        for label in new_labels:
            b_layout.add_widget(label)
        return height

class AuxilaryVariablesExample(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = commonMethods.niceLayout(width,'auxilaryVariablesExample', os.path.dirname(__file__))
        for label in new_labels:
            b_layout.add_widget(label)
        return height

    def runSimulation(self):
        _thread.start_new_thread(commonMethods.runSimulation,('projects/moose/tutorials/darcy_thermo_mech/step01_diffusion/problems/step1.i',))

class AuxilaryVariablesProblem(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = commonMethods.niceLayout(width,'auxilaryVariablesProblem', os.path.dirname(__file__))
        for label in new_labels:
            b_layout.add_widget(label)
        return height

class AuxilaryVariablesSolution(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = commonMethods.niceLayout(width,'auxilaryVariablesSolution', os.path.dirname(__file__))
        for label in new_labels:
            b_layout.add_widget(label)
        return height

Builder.load_string("""
<AuxilaryVariablesOverview>
    name: 'auxilary_variables_overview'
    id: auxilary_variables_overview
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                id: tester
                orientation: 'vertical'
                size_hint_y: None
                height: auxilary_variables_overview.addText(root.width)
        StackLayout:
            orientation: 'rl-bt'
            size_hint_y: None
            height: 50
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Next'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'auxilary_variables_member_variables'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Previous'
                background_color: 0,0,0,1

<AuxilaryVariablesMemberVariables>
    name: 'auxilary_variables_member_variables'
    id: auxilary_variables_member_variables
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                id: tester
                orientation: 'vertical'
                size_hint_y: None
                height: auxilary_variables_member_variables.addText(root.width)
        StackLayout:
            orientation: 'rl-bt'
            size_hint_y: None
            height: 50
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Next'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'auxilary_variables_member_functions'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Previous'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'auxilary_variables_overview'

<AuxilaryVariablesMemberFunctions>
    name: 'auxilary_variables_member_functions'
    id: auxilary_variables_member_functions
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                id: tester
                orientation: 'vertical'
                size_hint_y: None
                height: auxilary_variables_member_functions.addText(root.width)
        StackLayout:
            orientation: 'rl-bt'
            size_hint_y: None
            height: 50
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Next'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'auxilary_variables_example'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Previous'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'auxilary_variables_member_variables'

<AuxilaryVariablesExample>
    name: 'auxilary_variables_example'
    id: auxilary_variables_example
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                id: tester
                orientation: 'vertical'
                size_hint_y: None
                height: auxilary_variables_example.addText(root.width)
        StackLayout:
            orientation: 'rl-bt'
            size_hint_y: None
            height: 50
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Next'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'auxilary_variables_problem'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Previous'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'auxilary_variables_member_functions'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Run\\nSimulation'
                halign: 'center'
                on_release: auxilary_variables_example.runSimulation()

<AuxilaryVariablesProblem>
    name: 'auxilary_variables_problem'
    id: auxilary_variables_problem
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                id: tester
                orientation: 'vertical'
                size_hint_y: None
                height: auxilary_variables_problem.addText(root.width)
        StackLayout:
            orientation: 'rl-bt'
            size_hint_y: None
            height: 50
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Next'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'auxilary_variables_solution'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Previous'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'auxilary_variables_example'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Run\\nSimulation'
                halign: 'center'

<AuxilaryVariablesSolution>
    name: 'auxilary_variables_solution'
    id: auxilary_variables_solution
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                id: tester
                orientation: 'vertical'
                size_hint_y: None
                height: auxilary_variables_solution.addText(root.width)
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
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'auxilary_variables_problem'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Run\\nSimulation'
                halign: 'center'
""", filename = "auxilaryVariables.kv")
