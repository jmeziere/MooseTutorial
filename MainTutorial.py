from kivy.uix.screenmanager import ScreenManager, Screen

class InitScreen(Screen):
    pass

class AboutMoose(Screen):
    def getAboutMooseString(self):
        with open('AboutMoose.txt','r') as file:
            data = file.read()
        return data

class AboutTutorial(Screen):
    def getAboutTutorialString(self):
        with open('AboutTutorial.txt','r') as file:
            data = file.read()
        return data
