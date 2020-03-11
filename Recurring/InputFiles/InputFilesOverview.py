from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from pylatexenc.latex2text import LatexNodes2Text
from commonMethods import niceLayout

class InputFilesOverview(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = niceLayout(width,'InputFilesOverview1.txt', 'Recurring/InputFiles/')
        for label in new_labels:
            b_layout.add_widget(label)
        return height

# class InputFilesMemberVariables(Screen):
#     def getKernelsOverviewString(self):
#         with open('kernelsMemberVariables.txt') as file:
#             data = file.read()
#         return data

# class KernelsMemberFunctions(Screen):
#     def getKernelsOverviewString(self):
#         with open('kernelsMemberFunctions.txt') as file:
#             data = file.read()
#         return data

class InputFileExample(Screen):
    def getKernelsOverviewString(self):
        with open('InputFilesExample.txt') as file:
            data = file.read()
        return data

class InputFileProblem(Screen):
    def getKernelsOverviewString(self):
        with open('InputFilesProblem.txt') as file:
            data = file.read()
        return data

class InputFileSolution(Screen):
    def getKernelsOverviewString(self):
        with open('InputFilesSolution.txt') as file:
            data = file.read()
        return data
