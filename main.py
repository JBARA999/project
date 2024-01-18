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
        
            if self.final_result:
                self.show_data()    
        
        
    def show_data(self):
        self.object_style.lbl1['text']=self.final_result[0]+'-'+self.final_result[1]
        self.object_style.lbl2['text']=("{:.0f}°C , {:.0f}°F".format(self.final_result[3] , self.final_result[4]))
        self.object_style.lbl3['text']= self.final_result[5]
        self.object_style.lbl4['text']= self.final_result[6]
        self.object_style.lbl5['text']=self.final_result[7]
        self.object_style.lbl6['text']='| humidity'
        
        
        self.label_temp_celcuis = Label(self.root, font=('popins',25),bg='white',fg='red',text="{:.0f}°C".format(self.final_result[3]))
        self.label_temp_celcuis.place(x=500,y=200)
        
        
        self.label_humidity = Label(self.root , text=f"{self.final_result[8]}",font=('poppins',16),fg='black').place(x=550,y=305)
        
        
        
        
            

if __name__ == "__main__": 
  app = Tk()
  main_class=Main(app)
  app.mainloop()

