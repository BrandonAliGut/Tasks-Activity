from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.lang import Builder
from kivymd.uix.relativelayout import MDRelativeLayout
from datetime import date
from kivy.properties import StringProperty


#importar archivo py

from ScreenApp.tasks import TasksGroupDay
from  sqlcontroller.Controllersql import Tasks as SQL
from component.screen_view_all import Day_list

#carga de archibos kv
Builder.load_file("kv/welcome.kv")
Builder.load_file("main.kv")
Builder.load_file("component/kvcomponent_view.kv")
from kivy.core.window import Window
Window.size = (425, 750)

conex_sql = SQL()


class Welcome(Screen):
    def __init__(self, **kw):
        super(Welcome, self).__init__(**kw)


class WindowManager(ScreenManager):
    pass
class Add_day(MDRelativeLayout):
    pass
class Home(Screen):
    Day= None
    wm = None
    add_day_botton= None
    def __init__(self,**keyword):
        super(Home, self).__init__()
        Clock.schedule_once(lambda dt: [self.start(),self.update_screen()],2)
        self.wn = keyword["wm"]
        
        
        
        
    def update_screen(self,interval = 0.01):
        self.ids.days_gridlayout.clear_widgets()
        Clock.schedule_once(lambda dt: [self.start()],interval)
        
    def start(self):
        conex_sql = SQL()
        if not self.add_day_botton:
            self.add_day_botton = Add_day()
            self.ids.taskdayid.add_widget(self.add_day_botton)

        for day in reversed(conex_sql.viewtableday()):
            try:
                self.ids.days_gridlayout.add_widget(Day_list(
                    id=str(day[0]),
                    day=str(day[1]),
                    stado =str(day[2]),
                    date_at=str(day[3]),
                    start = str(day[4]),
                    end = str(day[5]),
                    date_end = str(day[6])
                    
                    ))
            
                if str(day[3]) == str(date.today()):
                    try:
                        self.ids.taskdayid.remove_widget(self.add_day_botton)
                        self.add_day_botton= None
                    except:
                        pass
            except:
                pass
    
    
    

class MyApp(MDApp):

    def build(self):

        # Create a list of all screen, loop through it and add it to the screenmanager
        # and return the screenmanager.
        self.wm = WindowManager()
        self.HOME = Home(wm=self.wm)
        screens = [
            Welcome(),
            self.HOME
        ]
        Clock.schedule_once(lambda dt: self.Inicio(),4)
        for screen in screens:
            self.wm.add_widget(screen)

        return self.wm
    def update(self):
        self.HOME.update_screen()
    def Inicio(self):
        print("si")
        self.root.current="Home"
    def irregister(self,id,activo):
        if activo == "no":
            print("usted no puede acceder a este registro")
        else:
            print("is")
            
    def day_lock(self,id):
        sql=SQL()
        sql.update_dayDB(id)
        self.update()
    def delete(self,day,activo):
        if activo != "no":
            conex_sql.delete('day',day)
            self.update()
    def add_widget_day(self):
        conex_sql.add_dayDB()
        self.update()
if __name__=="__main__":
    MyApp().run()