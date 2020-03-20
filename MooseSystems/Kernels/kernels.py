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
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = niceLayout(width,'kernelsMemberVariables.txt', 'MooseSystems/Kernels/')
        for label in new_labels:
            b_layout.add_widget(label)
        return height

class KernelsMemberFunctions(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = niceLayout(width,'kernelsMemberFunction.txt', 'MooseSystems/Kernels/')
        for label in new_labels:
            b_layout.add_widget(label)
        return height

class KernelsExample(Screen):
    def addText(self, width):
        b_layout = self.ids.tester
        (new_labels, height) = niceLayout(width,'kernelsExample.txt', 'MooseSystems/Kernels/')
        for label in new_labels:
            b_layout.add_widget(label)
        return height

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
