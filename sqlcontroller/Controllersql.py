import sqlite3 as sql
from datetime import date,datetime
#from kivy.clock import Clock
class Tasks:
    cursor = None
    conn= None
    def __init__(self,**args):
        super(Tasks,self).__init__(**args)
        self.open()
        #Clock.schedule_once(lambda dt: self.close_sql(),0.1)
        try:
            self.CreateTable() 
        except:
            pass
        
        #self.add_dayDB()
        #self.add_tasksDB()
        #self.viewtableday("lock_id",'tasks',4)
        #self.close_sql()
        
        
    
    def open(self):
        self.conn = sql.connect("Tasks_Activity.db")
        self.conn.commit()
        self.cursor = self.conn.cursor()
    def close_sql(self):
        self.conn.close()
        return True
        
    def CreateTable(self):
        
        self.cursor.execute(
            """
            CREATE TABLE day(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                day INT,
                Active_date CHAR(2) Null default('no'),
                date_at CHAR(20),
                start CHAR(20),
                end CHAR(20),
                date_up CHAR(20)
            )
            """
        )
        self.cursor.execute(
            '''
                CREATE TABLE tasks(
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    id_pk INTERGET NOT NULL,
                    name CHAR(50) NOT NULL,
                    contexto TEXT,
                    Active_date CHAR(2) Null default('no'),
                    date_at CHAR(20),
                    date_up CHAR(20),
                    FOREIGN KEY (id_pk) REFERENCES day(id)
        
                    
                )
            '''
        )
        
  
    def time(self):
        time = datetime.now()
        time_day = (str(str(time.hour)+":"+str(time.minute)))
        return time_day
    def add_dayDB(self):
        def add(sl):
            data = (sl,"si",date.today(),self.time())
            sqlconuslt ="insert into day(day,Active_date, date_at, start) values (?,?,?,?)"
            self.cursor.execute(sqlconuslt,data)
            self.conn.commit()
        self.cursor.execute("select * from day order by id desc limit 1")     
        __row = self.cursor.fetchall()
        count= 0
        print(__row)
        if not __row:
            count = 1
            add(count)
            
        for sl in __row:
            sld = sl[1] +1
            add( sld )
        
    def update_dayDB(self,pk):
    
        datatime = (self.time(),pk)

        datasql=self.viewtableday("lock_id","day",pk)
        sqlconuslt =  "UPDATE day SET Active_date=  ?,date_up = ? WHERE rowid = ?"
        sql_end = "UPDATE day SET end=  ? WHERE rowid = ?"
        
        for sqlviw in datasql:
            data = "si" if sqlviw[2] != "si" else "no"
            
            
            if not sqlviw[5] and sqlviw[2] != "no":
                
                self.cursor.execute(sql_end,datatime)
                
                self.conn.commit()
                
                
            data = (data,date.today(), pk)
            a=self.cursor.execute(
            sqlconuslt, data
        )
        self.conn.commit()
    
    def add_tasksDB(self):
        self.cursor.execute("insert into tasks(id_pk,name,contexto,Active_date, date_at, date_up) values ('3','tersera tarea','otro estudio','no',' 00-00-0000', '00-00-0000')")
        self.conn.commit()
        
        
    def allselectlock_id(self,__table,__a=None,__id=None):
        if __table != "lock_id":
            self.cursor.execute("select * from {} ".format(__table))
        else:
             self.cursor.execute("select * from {} where id= {} ".format(__a,__id))     
        __row = self.cursor.fetchall()
        if not __row:
            __row = [
                {
                 "error":201   
                }
            ] 
        return __row
    def viewtableday(self,__type="day",__table = None, __pk=None):
        
        if not __table and __type == "day":
            __table = "day"
        if not __pk:
            __pk = int()
            
        if __type == "day":
            return self.allselectlock_id(str(__type))
        elif __type == "tasks":
            return self.allselectlock_id(str(__type))
        elif __type == "all":
            for __a in __table:
                return self.allselectlock_id(str(__a))
                
        elif __type == "lock_id":
            return self.allselectlock_id("lock_id",str(__table),__pk)

        
    def locking(self):
        
        self.cursor.execute("select * from tasks where id_pk== 1")
        row = self.cursor.fetchall()
        print(row)

    #OCTIMIZAR ESTA PARTE DELETE
    def delete(self,table,day):
        def table_delete(table, day):
            self.cursor.execute("""DELETE FROM {t} where id = {d}""".format(t=table, d=day) )
            self.conn.commit()
            
        
        
        if table == "day":
            table_delete(table, day)
        elif table == "tasks":
            table_delete(table, day)
        else: 
            pass

        
