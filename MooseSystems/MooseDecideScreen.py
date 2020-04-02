from kivy.lang import Builder
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "Actions"))
import actions
sys.path.append(os.path.join(os.path.dirname(__file__), "AuxiliaryKernels"))
import auxiliaryKernels
sys.path.append(os.path.join(os.path.dirname(__file__), "AuxiliaryVariables"))
import auxiliaryVariables
sys.path.append(os.path.join(os.path.dirname(__file__), "BoundaryConditions"))
import boundaryConditions
sys.path.append(os.path.join(os.path.dirname(__file__), "Constraints"))
import constraints
sys.path.append(os.path.join(os.path.dirname(__file__), "Controls"))
import controls
sys.path.append(os.path.join(os.path.dirname(__file__), "Dampers"))
import dampers
sys.path.append(os.path.join(os.path.dirname(__file__), "DiracKernels"))
import diracKernels
sys.path.append(os.path.join(os.path.dirname(__file__), "DiscontinousGalerkinKernels"))
import discontinousGalerkinKernels
sys.path.append(os.path.join(os.path.dirname(__file__), "Executioner"))
import executioner
sys.path.append(os.path.join(os.path.dirname(__file__), "Functions"))
import functions
sys.path.append(os.path.join(os.path.dirname(__file__), "GeomSearch"))
import geomSearch
sys.path.append(os.path.join(os.path.dirname(__file__), "Indicators"))
import indicators
sys.path.append(os.path.join(os.path.dirname(__file__), "InitialConditions"))
import initialConditions
sys.path.append(os.path.join(os.path.dirname(__file__), "InterfaceKernels"))
import interfaceKernels
sys.path.append(os.path.join(os.path.dirname(__file__), "Kernels"))
import kernels
sys.path.append(os.path.join(os.path.dirname(__file__), "Markers"))
import markers
sys.path.append(os.path.join(os.path.dirname(__file__), "Materials"))
import materials
sys.path.append(os.path.join(os.path.dirname(__file__), "Mesh"))
import mesh
sys.path.append(os.path.join(os.path.dirname(__file__), "MeshModifiers"))
import meshModifiers
sys.path.append(os.path.join(os.path.dirname(__file__), "MultiApps"))
import multiApps
sys.path.append(os.path.join(os.path.dirname(__file__), "NodalKernels"))
import nodalKernels
sys.path.append(os.path.join(os.path.dirname(__file__), "Outputs"))
import outputs
sys.path.append(os.path.join(os.path.dirname(__file__), "Postprocessors"))
import postprocessors
sys.path.append(os.path.join(os.path.dirname(__file__), "Preconditioners"))
import preconditioners
sys.path.append(os.path.join(os.path.dirname(__file__), "Predictors"))
import predictors
sys.path.append(os.path.join(os.path.dirname(__file__), "Splits"))
import splits
sys.path.append(os.path.join(os.path.dirname(__file__), "TimeIntegrators"))
import timeIntegrators
sys.path.append(os.path.join(os.path.dirname(__file__), "TimeSteppers"))
import timeSteppers
sys.path.append(os.path.join(os.path.dirname(__file__), "Transfers"))
import transfers
sys.path.append(os.path.join(os.path.dirname(__file__), "UserObjects"))
import userObjects
sys.path.append(os.path.join(os.path.dirname(__file__), "Variables"))
import variables

Builder.load_string("""
<MooseDecideScreen@Screen>
    name: 'moose_decide_screen'
    id: moose_decide_screen
    ScrollView:
        orientation: 'tb-lr'
        size_hint_x: None
        width: 220
        do_scroll_y: True
        do_scroll_x: False
        StackLayout:
            size_hint_y: None
            height: 1000
            Button:
                id: action_button
                size_hint_y: None
                height: 30
                text: 'Actions'
                background_color: 0,0,0,1
                on_press: action_button.background_color = [1,1,1,1]
                on_release: App.get_running_app().root.ids.sub_sections.width = 0
                on_release: App.get_running_app().root.ids.moose_systems_button.background_color = [0,0,0,1]
                on_release: action_button.background_color = [0,0,0,1]
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'actions_overview'
            Button:
                id: aux_ker_button
                size_hint_y: None
                height: 30
                text: 'Auxiliary Kernels'
                background_color: 0,0,0,1
                on_press: aux_ker_button.background_color = [1,1,1,1]
                on_release: App.get_running_app().root.ids.sub_sections.width = 0
                on_release: App.get_running_app().root.ids.moose_systems_button.background_color = [0,0,0,1]
                on_release: aux_ker_button.background_color = [0,0,0,1]
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'auxiliary_kernels_overview'
            Button:
                id: aux_var_button
                size_hint_y: None
                height: 30
                text: 'Auxiliary Variables'
                background_color: 0,0,0,1
                on_press: aux_var_button.background_color = [1,1,1,1]
                on_release: App.get_running_app().root.ids.sub_sections.width = 0
                on_release: App.get_running_app().root.ids.moose_systems_button.background_color = [0,0,0,1]
                on_release: aux_var_button.background_color = [0,0,0,1]
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'auxiliary_variables_overview'
            Button:
                id: bc_button
                size_hint_y: None
                height: 30
                text: 'Boundary Conditions'
                background_color: 0,0,0,1
                on_press: bc_button.background_color = [1,1,1,1]
                on_release: App.get_running_app().root.ids.sub_sections.width = 0
                on_release: App.get_running_app().root.ids.moose_systems_button.background_color = [0,0,0,1]
                on_release: bc_button.background_color = [0,0,0,1]
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'boudary_conditions_overview'
            Button:
                id: constraint_button
                size_hint_y: None
                height: 30
                text: 'Constraints'
                background_color: 0,0,0,1
                on_press: constraint_button.background_color = [1,1,1,1]
                on_release: App.get_running_app().root.ids.sub_sections.width = 0
                on_release: App.get_running_app().root.ids.moose_systems_button.background_color = [0,0,0,1]
                on_release: constraint_button.background_color = [0,0,0,1]
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'constraints_overview'
            Button:
                id: control_button
                size_hint_y: None
                height: 30
                text: 'Controls'
                background_color: 0,0,0,1
                on_press: control_button.background_color = [1,1,1,1]
                on_release: App.get_running_app().root.ids.sub_sections.width = 0
                on_release: App.get_running_app().root.ids.moose_systems_button.background_color = [0,0,0,1]
                on_release: control_button.background_color = [0,0,0,1]
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'controls_overview'
            Button:
                id: damper_button
                size_hint_y: None
                height: 30
                text: 'Dampers'
                background_color: 0,0,0,1
                on_press: damper_button.background_color = [1,1,1,1]
                on_release: App.get_running_app().root.ids.sub_sections.width = 0
                on_release: App.get_running_app().root.ids.moose_systems_button.background_color = [0,0,0,1]
                on_release: damper_button.background_color = [0,0,0,1]
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'damper_overview'
            Button:
                id: dg_ker_button
                size_hint_y: None
                height: 30
                text: 'Discontinous Galerkin Kernels'
                background_color: 0,0,0,1
                on_press: dg_ker_button.background_color = [1,1,1,1]
                on_release: App.get_running_app().root.ids.sub_sections.width = 0
                on_release: App.get_running_app().root.ids.moose_systems_button.background_color = [0,0,0,1]
                on_release: dg_ker_button.background_color = [0,0,0,1]
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'discontinous_galerkin_kernels_overview'
            Button:
                id: dirac_ker_button
                size_hint_y: None
                height: 30
                text: 'Dirac Kernels'
                background_color: 0,0,0,1
                on_press: dirac_ker_button.background_color = [1,1,1,1]
                on_release: App.get_running_app().root.ids.sub_sections.width = 0
                on_release: App.get_running_app().root.ids.moose_systems_button.background_color = [0,0,0,1]
                on_release: dirac_ker_button.background_color = [0,0,0,1]
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'dirac_kernels_overview'
            Button:
                id: executioner_button
                size_hint_y: None
                height: 30
                text: 'Executioner'
                background_color: 0,0,0,1
                on_press: executioner_button.background_color = [1,1,1,1]
                on_release: App.get_running_app().root.ids.sub_sections.width = 0
                on_release: App.get_running_app().root.ids.moose_systems_button.background_color = [0,0,0,1]
                on_release: executioner_button.background_color = [0,0,0,1]
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'executioner_overview'
            Button:
                id: function_button
                size_hint_y: None
                height: 30
                text: 'Functions'
                background_color: 0,0,0,1
                on_press: function_button.background_color = [1,1,1,1]
                on_release: App.get_running_app().root.ids.sub_sections.width = 0
                on_release: App.get_running_app().root.ids.moose_systems_button.background_color = [0,0,0,1]
                on_release: function_button.background_color = [0,0,0,1]
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'functions_overview'
            Button:
                id: geom_search_button
                size_hint_y: None
                height: 30
                text: 'Geom Search'
                background_color: 0,0,0,1
                on_press: geom_search_button.background_color = [1,1,1,1]
                on_release: App.get_running_app().root.ids.sub_sections.width = 0
                on_release: App.get_running_app().root.ids.moose_systems_button.background_color = [0,0,0,1]
                on_release: geom_search_button.background_color = [0,0,0,1]
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'geom_search_overview'
            Button:
                id: indicator_button
                size_hint_y: None
                height: 30
                text: 'Indicators'
                background_color: 0,0,0,1
                on_press: indicator_button.background_color = [1,1,1,1]
                on_release: App.get_running_app().root.ids.sub_sections.width = 0
                on_release: App.get_running_app().root.ids.moose_systems_button.background_color = [0,0,0,1]
                on_release: indicator_button.background_color = [0,0,0,1]
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'indicators_overview'
            Button:
                id: ic_button
                size_hint_y: None
                height: 30
                text: 'Initial Conditions'
                background_color: 0,0,0,1
                on_press: aux_button.background_color = [1,1,1,1]
                on_release: App.get_running_app().root.ids.sub_sections.width = 0
                on_release: App.get_running_app().root.ids.moose_systems_button.background_color = [0,0,0,1]
                on_release: aux_button.background_color = [0,0,0,1]
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'initial_conditions_overview'
            Button:
                id: int_ker_button
                size_hint_y: None
                height: 30
                text: 'Interface Kernels'
                background_color: 0,0,0,1
                on_press: int_ker_button.background_color = [1,1,1,1]
                on_release: App.get_running_app().root.ids.sub_sections.width = 0
                on_release: App.get_running_app().root.ids.moose_systems_button.background_color = [0,0,0,1]
                on_release: int_ker_button.background_color = [0,0,0,1]
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'interface_kernels_overview'
            Button:
                id: kernel_button
                size_hint_y: None
                height: 30
                text: 'Kernels'
                background_color: 0,0,0,1
                on_press: kernel_button.background_color = [1,1,1,1]
                on_release: App.get_running_app().root.ids.sub_sections.width = 0
                on_release: App.get_running_app().root.ids.moose_systems_button.background_color = [0,0,0,1]
                on_release: kernel_button.background_color = [0,0,0,1]
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'kernels_overview'
            Button:
                id: marker_button
                size_hint_y: None
                height: 30
                text: 'Markers'
                background_color: 0,0,0,1
                on_press: marker_button.background_color = [1,1,1,1]
                on_release: App.get_running_app().root.ids.sub_sections.width = 0
                on_release: App.get_running_app().root.ids.moose_systems_button.background_color = [0,0,0,1]
                on_release: marker_button.background_color = [0,0,0,1]
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'markers_overview'
            Button:
                id: mesh_button
                size_hint_y: None
                height: 30
                text: 'Mesh'
                background_color: 0,0,0,1
                on_press: mesh_button.background_color = [1,1,1,1]
                on_release: App.get_running_app().root.ids.sub_sections.width = 0
                on_release: App.get_running_app().root.ids.moose_systems_button.background_color = [0,0,0,1]
                on_release: mesh_button.background_color = [0,0,0,1]
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'mesh_overview'
            Button:
                id: mesh_mod_button
                size_hint_y: None
                height: 30
                text: 'Mesh Modifiers'
                background_color: 0,0,0,1
                on_press: mesh_mod_button.background_color = [1,1,1,1]
                on_release: App.get_running_app().root.ids.sub_sections.width = 0
                on_release: App.get_running_app().root.ids.moose_systems_button.background_color = [0,0,0,1]
                on_release: mesh_mod_button.background_color = [0,0,0,1]
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'mesh_modifiers_overview'
            Button:
                id: multi_app_button
                size_hint_y: None
                height: 30
                text: 'MultiApps'
                background_color: 0,0,0,1
                on_press: multi_app_button.background_color = [1,1,1,1]
                on_release: App.get_running_app().root.ids.sub_sections.width = 0
                on_release: App.get_running_app().root.ids.moose_systems_button.background_color = [0,0,0,1]
                on_release: multi_app_button.background_color = [0,0,0,1]
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'multi_apps_overview'
            Button:
                id: nodal_ker_button
                size_hint_y: None
                height: 30
                text: 'Nodal Kernels'
                background_color: 0,0,0,1
                on_press: nodal_ker_button.background_color = [1,1,1,1]
                on_release: App.get_running_app().root.ids.sub_sections.width = 0
                on_release: App.get_running_app().root.ids.moose_systems_button.background_color = [0,0,0,1]
                on_release: nodal_ker_button.background_color = [0,0,0,1]
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'nodal_kernels_overview'
            Button:
                id: output_button
                size_hint_y: None
                height: 30
                text: 'Outputs'
                background_color: 0,0,0,1
                on_press: output_button.background_color = [1,1,1,1]
                on_release: App.get_running_app().root.ids.sub_sections.width = 0
                on_release: App.get_running_app().root.ids.moose_systems_button.background_color = [0,0,0,1]
                on_release: output_button.background_color = [0,0,0,1]
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'outputs_overview'
            Button:
                id: postprocessor_button
                size_hint_y: None
                height: 30
                text: 'Postprocessors'
                background_color: 0,0,0,1
                on_press: postprocessor_button.background_color = [1,1,1,1]
                on_release: App.get_running_app().root.ids.sub_sections.width = 0
                on_release: App.get_running_app().root.ids.moose_systems_button.background_color = [0,0,0,1]
                on_release: postprocessor_button.background_color = [0,0,0,1]
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'postprocessors_overview'
            Button:
                id: preconditioner_button
                size_hint_y: None
                height: 30
                text: 'Preconditioners'
                background_color: 0,0,0,1
                on_press: preconditioner_button.background_color = [1,1,1,1]
                on_release: App.get_running_app().root.ids.sub_sections.width = 0
                on_release: App.get_running_app().root.ids.moose_systems_button.background_color = [0,0,0,1]
                on_release: preconditioner_button.background_color = [0,0,0,1]
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'preconditionss_overview'
            Button:
                id: predictor_button
                size_hint_y: None
                height: 30
                text: 'Predictors'
                background_color: 0,0,0,1
                on_press: predictor_button.background_color = [1,1,1,1]
                on_release: App.get_running_app().root.ids.sub_sections.width = 0
                on_release: App.get_running_app().root.ids.moose_systems_button.background_color = [0,0,0,1]
                on_release: predictor_button.background_color = [0,0,0,1]
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'predictors_overview'
            Button:
                id: split_button
                size_hint_y: None
                height: 30
                text: 'Splits'
                background_color: 0,0,0,1
                on_press: split_button.background_color = [1,1,1,1]
                on_release: App.get_running_app().root.ids.sub_sections.width = 0
                on_release: App.get_running_app().root.ids.moose_systems_button.background_color = [0,0,0,1]
                on_release: split_button.background_color = [0,0,0,1]
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'splits_overview'
            Button:
                id: time_int_button
                size_hint_y: None
                height: 30
                text: 'Time Integrators'
                background_color: 0,0,0,1
                on_press: time_int_button.background_color = [1,1,1,1]
                on_release: App.get_running_app().root.ids.sub_sections.width = 0
                on_release: App.get_running_app().root.ids.moose_systems_button.background_color = [0,0,0,1]
                on_release: time_int_button.background_color = [0,0,0,1]
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'time_integrators_overview'
            Button:
                id: time_step_button
                size_hint_y: None
                height: 30
                text: 'Time Steppers'
                background_color: 0,0,0,1
                on_press: time_step_button.background_color = [1,1,1,1]
                on_release: App.get_running_app().root.ids.sub_sections.width = 0
                on_release: App.get_running_app().root.ids.moose_systems_button.background_color = [0,0,0,1]
                on_release: time_step_button.background_color = [0,0,0,1]
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'time_steppers_overview'
            Button:
                id: transfer_button
                size_hint_y: None
                height: 30
                text: 'Transfers'
                background_color: 0,0,0,1
                on_press: transfer_button.background_color = [1,1,1,1]
                on_release: App.get_running_app().root.ids.sub_sections.width = 0
                on_release: App.get_running_app().root.ids.moose_systems_button.background_color = [0,0,0,1]
                on_release: transfer_button.background_color = [0,0,0,1]
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'transfers_overview'
            Button:
                id: user_object_button
                size_hint_y: None
                height: 30
                text: 'User Objects'
                background_color: 0,0,0,1
                on_press: user_object_button.background_color = [1,1,1,1]
                on_release: App.get_running_app().root.ids.sub_sections.width = 0
                on_release: App.get_running_app().root.ids.moose_systems_button.background_color = [0,0,0,1]
                on_release: user_object_button.background_color = [0,0,0,1]
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'user_objects_overview'
            Button:
                id: variable_button
                size_hint_y: None
                height: 30
                text: 'Variables'
                background_color: 0,0,0,1
                on_press: variable_button.background_color = [1,1,1,1]
                on_release: App.get_running_app().root.ids.sub_sections.width = 0
                on_release: App.get_running_app().root.ids.moose_systems_button.background_color = [0,0,0,1]
                on_release: variable_button.background_color = [0,0,0,1]
                on_release: App.get_running_app().root.ids.tutorial_manager.current = 'variables_overview'
""", file = "MooseDecideScreen.kv")
