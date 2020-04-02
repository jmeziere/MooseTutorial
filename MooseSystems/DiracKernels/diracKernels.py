from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
import commonMethods
from kivy.lang import Builder
import os
import _thread

class DiracKernelsOverview(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = commonMethods.niceLayout(width,'diracKernelsOverview', os.path.dirname(__file__))
        for label in new_labels:
            b_layout.add_widget(label)
        return height

class DiracKernelsMemberVariables(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = commonMethods.niceLayout(width,'diracKernelsMemberVariables', os.path.dirname(__file__))
        for label in new_labels:
            b_layout.add_widget(label)
        return height

class DiracKernelsMemberFunctions(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = commonMethods.niceLayout(width,'diracKernelsMemberFunction', os.path.dirname(__file__))
        for label in new_labels:
            b_layout.add_widget(label)
        return height

class DiracKernelsExample(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = commonMethods.niceLayout(width,'diracKernelsExample', os.path.dirname(__file__))
        for label in new_labels:
            b_layout.add_widget(label)
        return height

    def runSimulation(self):
        _thread.start_new_thread(commonMethods.runSimulation,('projects/moose/tutorials/darcy_thermo_mech/step01_diffusion/problems/step1.i',))

class DiracKernelsProblem(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = commonMethods.niceLayout(width,'diracKernelsProblem', os.path.dirname(__file__))
        for label in new_labels:
            b_layout.add_widget(label)
        return height

class DiracKernelsSolution(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = commonMethods.niceLayout(width,'diracKernelsSolution', os.path.dirname(__file__))
        for label in new_labels:
            b_layout.add_widget(label)
        return height

Builder.load_string("""
<DiracKernelsOverview>
    name: 'dirac_kernels_overview'
    id: dirac_kernels_overview
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                id: tester
                orientation: 'vertical'
                size_hint_y: None
                height: dirac_kernels_overview.addText(root.width)
        StackLayout:
            orientation: 'rl-bt'
            size_hint_y: None
            height: 50
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Next'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'dirac_kernels_member_variables'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Previous'
                background_color: 0,0,0,1

<DiracKernelsMemberVariables>
    name: 'dirac_kernels_member_variables'
    id: dirac_kernels_member_variables
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                id: tester
                orientation: 'vertical'
                size_hint_y: None
                height: dirac_kernels_member_variables.addText(root.width)
        StackLayout:
            orientation: 'rl-bt'
            size_hint_y: None
            height: 50
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Next'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'dirac_kernels_member_functions'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Previous'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'dirac_kernels_overview'

<DiracKernelsMemberFunctions>
    name: 'dirac_kernels_member_functions'
    id: dirac_kernels_member_functions
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                id: tester
                orientation: 'vertical'
                size_hint_y: None
                height: dirac_kernels_member_functions.addText(root.width)
        StackLayout:
            orientation: 'rl-bt'
            size_hint_y: None
            height: 50
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Next'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'dirac_kernels_example'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Previous'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'dirac_kernels_member_variables'

<DiracKernelsExample>
    name: 'dirac_kernels_example'
    id: dirac_kernels_example
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                id: tester
                orientation: 'vertical'
                size_hint_y: None
                height: dirac_kernels_example.addText(root.width)
        StackLayout:
            orientation: 'rl-bt'
            size_hint_y: None
            height: 50
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Next'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'dirac_kernels_problem'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Previous'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'dirac_kernels_member_functions'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Run\\nSimulation'
                halign: 'center'
                on_release: dirac_kernels_example.runSimulation()

<DiracKernelsProblem>
    name: 'dirac_kernels_problem'
    id: dirac_kernels_problem
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                id: tester
                orientation: 'vertical'
                size_hint_y: None
                height: dirac_kernels_problem.addText(root.width)
        StackLayout:
            orientation: 'rl-bt'
            size_hint_y: None
            height: 50
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Next'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'dirac_kernels_solution'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Previous'
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'dirac_kernels_example'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Run\\nSimulation'
                halign: 'center'

<DiracKernelsSolution>
    name: 'dirac_kernels_solution'
    id: dirac_kernels_solution
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            BoxLayout:
                id: tester
                orientation: 'vertical'
                size_hint_y: None
                height: dirac_kernels_solution.addText(root.width)
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
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'dirac_kernels_problem'
            Button:
                size_hint: None, None
                height: 50
                width: 100
                text: 'Run\\nSimulation'
                halign: 'center'
""", filename = "diracKernels.kv")
