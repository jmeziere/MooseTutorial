from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
import commonMethods
from kivy.lang import Builder
import os
import _thread

class BoundaryConditionsOverview(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = commonMethods.niceLayout(width,'boundaryConditionsOverview', os.path.dirname(__file__))
        for label in new_labels:
            b_layout.add_widget(label)
        return height

class BoundaryConditionsMemberVariables(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = commonMethods.niceLayout(width,'boundaryConditionsMemberVariables', os.path.dirname(__file__))
        for label in new_labels:
            b_layout.add_widget(label)
        return height

class BoundaryConditionsMemberFunctions(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = commonMethods.niceLayout(width,'boundaryConditionsMemberFunction', os.path.dirname(__file__))
        for label in new_labels:
            b_layout.add_widget(label)
        return height

class BoundaryConditionsExample(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = commonMethods.niceLayout(width,'boundaryConditionsExample', os.path.dirname(__file__))
        for label in new_labels:
            b_layout.add_widget(label)
        return height

    def runSimulation(self):
        _thread.start_new_thread(commonMethods.runSimulation,('projects/moose/tutorials/darcy_thermo_mech/step01_diffusion/problems/step1.i',))

class BoundaryConditionsProblem(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = commonMethods.niceLayout(width,'boundaryConditionsProblem', os.path.dirname(__file__))
        for label in new_labels:
            b_layout.add_widget(label)
        return height

class BoundaryConditionsSolution(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = commonMethods.niceLayout(width,'boundaryConditionsSolution', os.path.dirname(__file__))
        for label in new_labels:
            b_layout.add_widget(label)
        return height

Builder.load_string("""
<BoundaryConditionsOverview>
    name: 'boundary_conditions_overview'
    id: boundary_conditions_overview
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                id: tester
                orientation: 'vertical'
                size_hint_y: None
                height: boundary_conditions_overview.addText(root.width)
        StackLayout:
            orientation: 'rl-bt'
            size_hint_y: None
            height: 50
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Next'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'boundary_conditions_member_variables'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Previous'
                background_color: 0,0,0,1

<BoundaryConditionsMemberVariables>
    name: 'boundary_conditions_member_variables'
    id: boundary_conditions_member_variables
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                id: tester
                orientation: 'vertical'
                size_hint_y: None
                height: boundary_conditions_member_variables.addText(root.width)
        StackLayout:
            orientation: 'rl-bt'
            size_hint_y: None
            height: 50
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Next'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'boundary_conditions_member_functions'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Previous'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'boundary_conditions_overview'

<BoundaryConditionsMemberFunctions>
    name: 'boundary_conditions_member_functions'
    id: boundary_conditions_member_functions
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                id: tester
                orientation: 'vertical'
                size_hint_y: None
                height: boundary_conditions_member_functions.addText(root.width)
        StackLayout:
            orientation: 'rl-bt'
            size_hint_y: None
            height: 50
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Next'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'boundary_conditions_example'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Previous'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'boundary_conditions_member_variables'

<BoundaryConditionsExample>
    name: 'boundary_conditions_example'
    id: boundary_conditions_example
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                id: tester
                orientation: 'vertical'
                size_hint_y: None
                height: boundary_conditions_example.addText(root.width)
        StackLayout:
            orientation: 'rl-bt'
            size_hint_y: None
            height: 50
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Next'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'boundary_conditions_problem'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Previous'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'boundary_conditions_member_functions'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Run\\nSimulation'
                halign: 'center'
                on_release: boundary_conditions_example.runSimulation()

<BoundaryConditionsProblem>
    name: 'boundary_conditions_problem'
    id: boundary_conditions_problem
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                id: tester
                orientation: 'vertical'
                size_hint_y: None
                height: boundary_conditions_problem.addText(root.width)
        StackLayout:
            orientation: 'rl-bt'
            size_hint_y: None
            height: 50
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Next'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'boundary_conditions_solution'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Previous'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'boundary_conditions_example'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Run\\nSimulation'
                halign: 'center'

<BoundaryConditionsSolution>
    name: 'boundary_conditions_solution'
    id: boundary_conditions_solution
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                id: tester
                orientation: 'vertical'
                size_hint_y: None
                height: boundary_conditions_solution.addText(root.width)
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
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'boundary_conditions_problem'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Run\\nSimulation'
                halign: 'center'
""", filename = "boundaryConditions.kv")
