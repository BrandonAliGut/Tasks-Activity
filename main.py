from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.lang import Builder

#importar archivo py

from ScreenApp.tasks import TasksGroupDay

#carga de archibos kv
Builder.load_file("kv/welcome.kv")
Builder.load_file("main.kv")
from kivy.core.window import Window
Window.size = (425, 750)


class Welcome(Screen):
    def __init__(self, **kw):
        super(Welcome, self).__init__(**kw)


class WindowManager(ScreenManager):
    pass

class Home(Screen):
    def __init__(self):
        super(Home, self).__init__()
        Clock.schedule_once(lambda dt: self.update_screen,0.1)
    def update_screen(self):
        pass

class MyApp(MDApp):

    def build(self):

        # Create a list of all screen, loop through it and add it to the screenmanager
        # and return the screenmanager.
        self.wm = WindowManager()
       
        screens = [
            Welcome(),
            Home()
        ]
        Clock.schedule_once(lambda dt: self.Inicio(),1)
        for screen in screens:
            self.wm.add_widget(screen)

        return self.wm
    def Inicio(self):
        print("si")
        self.root.current="Home"

if __name__=="__main__":
    MyApp().run()