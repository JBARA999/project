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
        
        
        
def get_data(self):
        
        self.url_api = requests.get(self.url.format(self.city_name.get(),self.API))
        if self.url_api:
            
            self.jsonData = self.url_api.json()
        
            self.city = self.jsonData['name']
            self.country = self.jsonData['sys']['country']
        
            self.temp_klv = self.jsonData['main']['temp']
            self.temp_celcuis = (self.temp_klv-273.15)
            self.temp_fehr = (self.temp_klv-273.15)*9/5+32
        
            self.weather = self.jsonData['weather'][0]['main']
        
            self.pressure = self.jsonData['main']['pressure']
        
            self.description = self.jsonData['weather'][0]['description']
        
            self.humidity = self.jsonData['main']['humidity']
        
            self.final_result = (
                self.city , self.country , self.temp_klv , self.temp_celcuis , self.temp_fehr , self.weather ,self.pressure , self.description , self.humidity
            )       
        
                
        
        
        

if __name__ == "__main__": 
  app = Tk()
  main_class=Main(app)
  app.mainloop()

