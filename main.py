from tkinter import *
from tkinter import messagebox
import requests
from datetime import datetime
import time
from style import Style

class Main:
    def __init__(self,root):



        self.root = root
        self.object_style = Style(self.root)

        
        self.variable_city=StringVar()
        
        
        self.city_name=Entry(self.root,font=('poppins',22),bg='#404040',border=0,fg='white',textvariable=self.variable_city)
        self.city_name.place(x=290,y=60)
        

        self.image_get = PhotoImage(file='images//get_data.png')
        self.button = Button(
            self.root , image=self.image_get , background='#404040' , borderwidth=0 , command=self.get_data).place(x=620,y=52)
        
        
        
        
        
        
        

if __name__ == "__main__": 
  app = Tk()
  main_class=Main(app)
  app.mainloop()

