from tkinter import *
from tkinter import font
import random
from web_scraping import date_list

from tkinter import *
from tkinter import font
import random
from web_scraping import *
from tkinter.font import Font


class App():
    def __init__(self, master):
        self.myString = StringVar()
        self.myString.set("Choose Your Date")
        self.myString2 = StringVar()
        self.myString2.set("Choose Your Movie")
        self.myString3 = StringVar()
        self.myString3.set("Choose Your Time")
        self.master = master
        self.newest_font = font.Font(family="Comic Sans MS", size=23)

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
        self.x = self.list_days.index(self.myString.get())
        self.y = self.list_links[self.x]
        self.movie_listings = movie_title(self.y)
        self.choose_movie = OptionMenu(self.master, self.myString2, *self.movie_listings)
        self.choose_movie.grid(row="3", column="2")
        self.submit_button.config(state="disabled")

        self.submit_button2.bind('<Button-1>', self.continuehour)
        self.submit_button2.grid(row="3", column="3")


        # if self.myString!="Choose Your Date":
        # self.choose_movie=OptionMenu(master,self.myString2)

    def continuehour(self, event=None):

        self.submit_button2.config(state="disabled")
        z=self.movie_listings.index(self.myString2.get())
        self.n=find_time(z,self.y)
        self.choose_time = OptionMenu(self.master, self.myString3, *self.n)
        self.choose_time.grid(row="4", column="2")

        self.submit_button3 = Label(text="Choose Time", bg="lightblue", fg="black")
        self.submit_button3.bind('<Button-1>', self.endfunc)
        self.submit_button3.grid(row="4", column="3")

    def endfunc(self,event=None):
        self.submit_button3.config(state="disabled")
        self.spinbox1=Spinbox(self.master,from_=1,to=6)
        self.spinbox1.grid(row="4",column="4")

        self.submit_button4 = Label(text="Buy Tickets",font=self.newest_font, bg="gold", fg="black")
        self.submit_button4.bind("<Button-1>",self.ginend)
        self.submit_button4.grid(row="1",column="4",rowspan="3")
    def ginend(self):
        


if __name__ == "__main__":
    root = Tk()
    root.title("Movie Scheduler")
    my_app = App(root)

    root.mainloop()