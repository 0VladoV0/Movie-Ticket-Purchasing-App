from tkinter import *
from tkinter import font
import random
from web_scraping import date_list

from tkinter import *
from tkinter import font
import random
from web_scraping import *


class App():
    def __init__(self, master):
        self.myString = StringVar()
        self.myString.set("Choose Your Date")
        self.myString2 = StringVar()
        self.myString2.set("Choose Your Movie")
        self.myString3 = StringVar()
        self.myString3.set("Choose Your Month")
        self.master = master

        self.list_days, self.list_links = date_list()

        print(self.list_days)

        self.title_font = font.Font(family="Comic Sans MS", size=17)
        self.new_font = font.Font(family="Comic Sans MS", size=23)

        self.choose_day = OptionMenu(master, self.myString, *self.list_days)
        self.choose_day.grid(row="2", column="2")

        self.submit_button = Label(text="Choose Date", bg="lightblue", fg="black")
        self.submit_button.bind('<Button-1>', self.continuemov)
        self.submit_button.grid(row="2", column="3")

        self.submit_button2 = Label(text="Choose Movie", bg="lightblue", fg="black")

    def continuemov(self, event=None):
        x = self.list_days.index(self.myString.get())
        y = self.list_links[x]
        movie_listings = movie_title(y)
        self.choose_movie = OptionMenu(self.master, self.myString2, *movie_listings)
        self.choose_movie.grid(row="3", column="2")
        self.submit_button.config(state="disabled")

        self.submit_button2.bind('<Button-1>', self.continuehour)
        self.submit_button2.grid(row="3", column="3")
        # if self.myString!="Choose Your Date":
        # self.choose_movie=OptionMenu(master,self.myString2)

    def continuehour(self, event=None):


if __name__ == "__main__":
    root = Tk()
    root.title("Movie Scheduler")
    my_app = App(root)

    root.mainloop()