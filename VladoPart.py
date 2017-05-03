from tkinter import *
from tkinter import font
import random

class App():



    def __init__(self,master):
        self.myString = StringVar()
        self.answer=StringVar()
        self.myString.set("Choose Your Movie")

        self.title_font = font.Font(family="Comic Sans MS", size=17)
        self.new_font = font.Font(family="Comic Sans MS", size=23)

        self.choose_movie= OptionMenu(master,self.myString,"One","Two","three").grid(row="2",column="2")





if __name__ == "__main__":
    root = Tk()
    root.title("Movie Scheduler")
    my_app = App(root)


    root.mainloop()

