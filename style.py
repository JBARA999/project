from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import requests
class Style:
    def __init__(self,master):
        self.master = master
        self.master.geometry("900*800+650+100")
        self.master.title("whatherApp")
        self.master.configure(background = "powred blue")