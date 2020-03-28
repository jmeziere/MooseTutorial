import sys
import os
from kivy.lang import Builder

sys.path.append(os.path.join(os.path.dirname(__file__), "InputFiles"))
import InputFilesOverview

Builder.load_string("""
<RecurringThemesScreen@Screen>
    name: 'recurring_themes_screen'
    id: recurring_themes_screen
    StackLayout:
        orientation: 'tb-lr'
        size_hint_x: None
        width: 100
        Button:
            id: input_files_button
            size_hint_y: None
            height: 30
            text: 'Input Files'
            background_color: 0,0,0,1
            on_press: input_files_button.background_color = [1,1,1,1]
            on_release: App.get_running_app().root.ids.sub_sections.width = 0
            on_release: App.get_running_app().root.ids.recurring_themes_button.background_color = [0,0,0,1]
            on_release: input_files_button.background_color = [0,0,0,1]
            on_release: App.get_running_app().root.ids.tutorial_manager.current = 'input_files_overview'
        Button:
            id: c_files_button
            size_hint_y: None
            height: 30
            text: 'C files'
            background_color: 0,0,0,1
            on_press: c_files_button.background_color = [1,1,1,1]
            on_release: App.get_running_app().root.ids.sub_sections.width = 0
            on_release: App.get_running_app().root.ids.recurring_themes_button.background_color = [0,0,0,1]
            on_release: c_files_button.background_color = [0,0,0,1]
            on_release: App.get_running_app().root.ids.tutorial_manager.current = 'needs_work'
        Button:
            id: h_files_button
            size_hint_y: None
            height: 30
            text: 'h files'
            background_color: 0,0,0,1
            on_press: h_files_button.background_color = [1,1,1,1]
            on_release: App.get_running_app().root.ids.sub_sections.width = 0
            on_release: App.get_running_app().root.ids.recurring_themes_button.background_color = [0,0,0,1]
            on_release: h_files_button.background_color = [0,0,0,1]
            on_release: App.get_running_app().root.ids.tutorial_manager.current = 'needs_work'
""", filename = "RecurringThemesScreen.kv")
