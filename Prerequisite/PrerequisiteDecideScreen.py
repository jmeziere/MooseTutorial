from kivy.lang import Builder

Builder.load_string("""
#:import App kivy.app.App
<PrerequisiteDecideScreen@Screen>
    name: 'prerequisite_decide_screen'
    id: prerequisite_decide_screen
    StackLayout:
        orientation: 'tb-lr'
        size_hint_x: None
        width: 200
        Button:
            id: fem_button
            size_hint_y: None
            height: 30
            text: 'Finite Element Overview'
            background_color: 0,0,0,1
            on_press: fem_button.background_color = [1,1,1,1]
            on_release: App.get_running_app().root.ids.sub_sections.width = 0
            on_release: App.get_running_app().root.ids.prerequisite_knowledge_button.background_color = [0,0,0,1]
            on_release: fem_button.background_color = [0,0,0,1]
        Button:
            id: weak_button
            size_hint_y: None
            height: 30
            text: 'Weak Form'
            background_color: 0,0,0,1
            on_press: weak_button.background_color = [1,1,1,1]
            on_release: App.get_running_app().root.ids.sub_sections.width = 0
            on_release: App.get_running_app().root.ids.prerequisite_knowledge_button.background_color = [0,0,0,1]
            on_release: weak_button.background_color = [0,0,0,1]
        Button:
            id: functional_button
            size_hint_y: None
            height: 30
            text: 'Functional Analysis'
            background_color: 0,0,0,1
            on_press: functional_button.background_color = [1,1,1,1]
            on_release: App.get_running_app().root.ids.sub_sections.width = 0
            on_release: App.get_running_app().root.ids.prerequisite_knowledge_button.background_color = [0,0,0,1]
            on_release: functional_button.background_color = [0,0,0,1]
""", filename = "PrerequisiteDecideScreen.kv")