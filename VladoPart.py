from tkinter import *
from tkinter import font
import random
from web_scraping import date_list

class App():



    def __init__(self,master):
        self.myString = StringVar()
        self.myString.set("Choose Your Date")
        self.myString2 = StringVar()
        self.myString2.set("Choose Your Date")
        self.myString3 = StringVar()
        self.myString3.set("Choose Your Month")

        self.title_font = font.Font(family="Comic Sans MS", size=17)
        self.new_font = font.Font(family="Comic Sans MS", size=23)

        self.choose_day= OptionMenu(master,self.myString, *date_list()).grid(row="2",column="2")




if __name__ == "__main__":
    root = Tk()
    root.title("Movie Scheduler")
    my_app = App(root)


    root.mainloop()

