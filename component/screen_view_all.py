from kivymd.uix.card import MDCard
from kivy.properties import StringProperty

class Day_list(MDCard):
    id= StringProperty()
    day = StringProperty()
    date_at = StringProperty()
    stado = StringProperty()
    start= StringProperty()
    end = StringProperty()
    date_end = StringProperty()
    def __init__(self, *args,**keyword):
        super(Day_list,self).__init__(*args)
        self.id = keyword['id']
        self.day = keyword['day']
        self.date_at = keyword['date_at']
        self.stado = keyword['stado']
        self.start = keyword['start']
        self.end = keyword['end']
        self.size_hint_y= None
        self.height= 80
        self.md_bg_color= 194/255, 196/255, 212/255, 0.241
        self.radius= [4,4,4,4]
    
                