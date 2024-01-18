from tkinter import *
from style import Style

class Main:
    def __init__(self,root):
        self.root = root
        self.object_style = Style(self.root)

if __name__ == "__main__": 
  app = Tk()
  main_class=Main(app)
  app.mainloop()