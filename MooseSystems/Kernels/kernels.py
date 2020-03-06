from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from pylatexenc.latex2text import LatexNodes2Text
from commonMethods import niceLayout

class KernelsOverview(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = niceLayout(width,'kernelsOverview.txt', 'MooseSystems/Kernels/')
        for label in new_labels:
            b_layout.add_widget(label)
        return height

class KernelsMemberVariables(Screen):
    def getKernelsOverviewString(self):
        with open('kernelsMemberVariables.txt') as file:
            data = file.read()
        return data

class KernelsMemberFunctions(Screen):
    def getKernelsOverviewString(self):
        with open('kernelsMemberFunctions.txt') as file:
            data = file.read()
        return data

class KernelsExample(Screen):
    def getKernelsOverviewString(self):
        with open('kernelsExample.txt') as file:
            data = file.read()
        return data

class KernelsProblem(Screen):
    def getKernelsOverviewString(self):
        with open('kernelsProblem.txt') as file:
            data = file.read()
        return data

class KernelsSolution(Screen):
    def getKernelsOverviewString(self):
        with open('kernelsSolution.txt') as file:
            data = file.read()
        return data
