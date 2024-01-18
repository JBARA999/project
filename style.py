from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

class Style:
    def __init__(self,master):
        self.master = master


        self.master.geometry("900*800+650+100")
        self.master.title("whatherApp")
        self.master.configure(background = "powred blue")

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

        self.add_titles()
        
        
def add_titles(self):
        self.location = Label(self.master , text='location' , bg='#1ab5ef' , font=('popins',12,'bold'),foreground='white').place(x=180,y=660)    
        self.temperature = Label(self.master , text='temperature' , bg='#1ab5ef' , font=('popins',12,'bold'),foreground='white').place(x=320,y=660)
        self.weather = Label(self.master , text='weather' , bg='#1ab5ef' , font=('popins',12,'bold'),foreground='white').place(x=500,y=660)
        self.pressure = Label(self.master , text='pressure' , bg='#1ab5ef' , font=('popins',12,'bold'),foreground='white').place(x=630,y=660)
        self.description = Label(self.master , text='description' , bg='#1ab5ef' , font=('popins',12,'bold'),foreground='white').place(x=760,y=660)
        



        self.lbl1 = Label(self.master, text='....', bg='#1ab5ef', font=('popins', 16, 'bold'), foreground='#000000')
        self.lbl1.place(x=190, y=690)
        self.lbl2 = Label(self.master, text='....', bg='#1ab5ef', font=('popins', 16, 'bold'), foreground='#000000')
        self.lbl2.place(x=350,y=690)
        self.lbl3 = Label(self.master, text='....', bg='#1ab5ef', font=('popins', 16, 'bold'), foreground='#000000')
        self.lbl3.place(x=520,y=690)
        self.lbl4 = Label(self.master, text='....', bg='#1ab5ef', font=('popins', 16, 'bold'), foreground='#000000')
        self.lbl4.place(x=650,y=690)
        self.lbl5 = Label(self.master, text='....', bg='#1ab5ef', font=('popins', 16, 'bold'), foreground='#000000')
        self.lbl5.place(x=780,y=690)
        self.lbl6 = Label(self.master, text='....', bg='#f0f7fa', font=('popins', 16, 'bold'), foreground='#000000')
        self.lbl6.place(x=575,y=300)

        


