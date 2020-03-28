from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
import sys
import os

sys.path.append(os.path.dirname(__file__))

sys.path.append(os.path.join(os.path.dirname(__file__), "Main"))
import MainTutorial

sys.path.append(os.path.join(os.path.dirname(__file__), "MooseSystems"))
import MooseDecideScreen

sys.path.append(os.path.join(os.path.dirname(__file__), "Installation"))
import InstallationDecideScreen

sys.path.append(os.path.join(os.path.dirname(__file__), "Recurring"))
import RecurringThemesScreen

sys.path.append(os.path.join(os.path.dirname(__file__), "Prerequisite"))
import PrerequisiteDecideScreen

from kivy.uix.screenmanager import ScreenManager, Screen

class MainScreen(Screen):
    pass

presentation = Builder.load_string("""
#:import NoTransition kivy.uix.screenmanager.NoTransition
ScreenManager:
    MainScreen:
        name: 'main_screen'
        id: main_screen
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: 'MOOSE Tutorial'
                font_size: 75
                height: 100
                width: root.width
                size_hint: None, None
                valign: 'center'
                halign:'center'
            BoxLayout:
                StackLayout:
                    orientation: 'tb-lr'
                    size_hint_x: None
                    width: 175
                    Button:
                        id: main_button
                        background_color: 0,0,0,1
                        height: 30
                        size_hint_y: None
                        text: 'Main'
                        on_press: main_button.background_color = [1,1,1,1]
                        on_press: installation_button.background_color = [0,0,0,1]
                        on_press: prerequisite_knowledge_button.background_color = [0,0,0,1]
                        on_press: recurring_themes_button.background_color = [0,0,0,1]
                        on_press: moose_systems_button.background_color = [0,0,0,1]
                        on_press: sub_sections.width = 0
                        on_release: main_button.background_color = [0,0,0,1]
                        on_release: tutorial_manager.current = 'init_screen'
                    Button:
                        id: installation_button
                        background_color: 0,0,0,1
                        height: 30
                        size_hint_y: None
                        text: 'Installation'
                        on_press: installation_button.background_color = [1,1,1,1] if installation_button.background_color == [0,0,0,1] else [0,0,0,1]
                        on_press: prerequisite_knowledge_button.background_color = [0,0,0,1]
                        on_press: recurring_themes_button.background_color = [0,0,0,1]
                        on_press: moose_systems_button.background_color = [0,0,0,1]
                        on_press: sub_section_manager.current = 'installation_decide_screen'
                        on_press: sub_sections.width = 100  if installation_button.background_color == [0,0,0,1] else 0
                    Button:
                        id: prerequisite_knowledge_button
                        background_color: 0,0,0,1
                        height: 30
                        size_hint_y: None
                        text: 'Prerequisite Knowledge'
                        on_press: installation_button.background_color = [0,0,0,1]
                        on_press: prerequisite_knowledge_button.background_color = [1,1,1,1] if prerequisite_knowledge_button.background_color == [0,0,0,1] else [0,0,0,1]
                        on_press: recurring_themes_button.background_color = [0,0,0,1]
                        on_press: moose_systems_button.background_color = [0,0,0,1]
                        on_press: sub_section_manager.current = 'prerequisite_decide_screen'
                        on_press: sub_sections.width = 200  if prerequisite_knowledge_button.background_color == [0,0,0,1] else 0
                    Button:
                        id: recurring_themes_button
                        background_color: 0,0,0,1
                        height: 30
                        size_hint_y: None
                        text: 'Recurring Themes'
                        on_press: installation_button.background_color = [0,0,0,1]
                        on_press: prerequisite_knowledge_button.background_color = [0,0,0,1]
                        on_press: recurring_themes_button.background_color = [1,1,1,1] if recurring_themes_button.background_color == [0,0,0,1] else [0,0,0,1]
                        on_press: moose_systems_button.background_color = [0,0,0,1]
                        on_press: sub_section_manager.current = 'recurring_themes_screen'
                        on_press: sub_sections.width = 100  if recurring_themes_button.background_color == [0,0,0,1] else 0
                    Button:
                        id: moose_systems_button
                        background_color: 0,0,0,1
                        height: 30
                        size_hint_y: None
                        text: 'MOOSE Systems'
                        on_press: installation_button.background_color = [0,0,0,1]
                        on_press: prerequisite_knowledge_button.background_color = [0,0,0,1]
                        on_press: recurring_themes_button.background_color = [0,0,0,1]
                        on_press: moose_systems_button.background_color = [1,1,1,1] if moose_systems_button.background_color == [0,0,0,1] else [0,0,0,1]
                        on_press: sub_section_manager.current = 'moose_decide_screen'
                        on_press: sub_sections.width = 220  if moose_systems_button.background_color == [0,0,0,1] else 0
                BoxLayout:
                    id: sub_sections
                    size_hint_x: None
                    width: 0
                    ScreenManager:
                        transition: NoTransition()
                        id: sub_section_manager
                        InstallationDecideScreen:
                        PrerequisiteDecideScreen:
                        MooseDecideScreen:
                        RecurringThemesScreen:
                BoxLayout:
                    ScreenManager:
                        id: tutorial_manager
                        transition: NoTransition()
                        # Main
                            # Moose Introduction
                        InitScreen:
                        AboutInl:
                        AboutMoose:
                        AboutTutorial:
                        # Installation
                            # Linux
                        Mint19:
                        Mint18:
                        Ubuntu18_04:
                        Ubuntu16_04:
                        Fedora:
                            # mac
                        # Prerequisites
                        # Recurring Themes
                            # Input Files
                        InputFilesOverview:
                        InputFilesExample:
                        InputFilesProblem:
                        InputFilesSolution:
                        # MOOSE Systems
                            # Actions
                            # Auxiliary Kernels
                            # Auxiliary Variables
                            # Boundary Conditions
                            # Constraints
                            # Controls
                            # Dampers
                            # Discontinous Galerkin Kernels
                            # Dirac Kernels
                            # Executioner
                            # Functions
                            # Geom Search
                            # Initial Conditions
                            # Indicators
                            # Interface Kernels
                            # Kernels
                        KernelsOverview:
                        KernelsMemberVariables:
                        KernelsMemberFunctions:
                        KernelsExample:
                        KernelsProblem:
                        KernelsSolution:
                            # Markers
                            # Materials
                            # MeshModifiers
                            # MultiApps
                            # Nodal Kernels
                            # Outputs
                            # Postprocessors
                            # Preconditioners
                            # Predictors
                            # Splits
                            # Time Integrators
                            # Time Steppers
                            # Transfers
                            # User Objects
                            # Variables

                        # Needs Additional Development
                        NeedsWork:
<NeedsWork@Screen>
    name: 'needs_work'
    id: needs_work
    Label:
        text: 'This page needs development!'
""", file = "main.kv")

class MainApp(App):
    def build(self):
        return presentation

if __name__ == '__main__':
    MainApp().run()
