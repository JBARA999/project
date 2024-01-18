from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import requests
class Style:
    def __init__(self,master):
        self.master = master
        self.master.geometry("1000x800+400+100")
        self.master.title("meteo project")
        self.master.resizable(width=False , height=False)
        self.master.iconbitmap('images//weather.ico')
        
        
        
        self.image_city = PhotoImage(file='images//search.png')
        self.label_city = Label(self.master , image=self.image_city )
        self.label_city.place(x=250,y=40)


        self.logo_image = PhotoImage(file='images//logo.png')
        self.label_logo = Label(self.master , image=self.logo_image ).place(x=300,y=200)

        self.box_image = PhotoImage(file='images//box.png')
        self.box_logo = Label(self.master , image=self.box_image ).place(x=120,y=640)