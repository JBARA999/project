from tkinter import *
from style import Style
from tkinter import messagebox
import requests

class Main:
    def __init__(self,root):
        self.root = root
        self.url='https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
        self.API='06051f3cad0ad7ba821ba795bf6d124f'
        self.object_style = Style(self.root)
        
        self.variable_city=StringVar()
        
        
        self.city_name=Entry(self.root,font=('poppins',22),bg='#404040',border=0,fg='white',textvariable=self.variable_city)
        self.city_name.place(x=290,y=60)
        
        
        
if __name__ == "__main__": 
  app = Tk()
  main_class=Main(app)
  app.mainloop()