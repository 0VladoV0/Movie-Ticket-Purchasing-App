'''
from tkinter import *
import csv



#movies   name  tickets available   date   time

#MAKE SURE TO DO THE FILE.CLOSE THING WHEN SENDING THE STUFF in

movies = []
list = []

def purchase(date, movie, time, tickets):
    movie_list = []
    def file_opening():
        file = open("ledger.csv", "r")

        reader = csv.reader(file, delimiter=',')


        for line in reader:
            movie_list.append(line)
        print(movie_list)
        file.close()
        return movie_list


   
    #watched = []
    movie_list.append(date)
    movie_list.append(movie)
    movie_list.append(time)
    movie_list.append(tickets)


    def ticket_check(tickets):
        file_opening()
        total = 0
        if tickets > 10:
            print("you cant buy that many tickets")
        else:
            total += tickets
            movie_list.append(total)

    #def more_checking(tickets, date):
     #   daily_tickets = 0
      #  if date == 'placeholder':




    ticket_check(tickets)
    return movie_list

result = purchase("wednesday", "star wars", 13, 10)
movies.append(result)
print(movies)

result = purchase("thursday", "batman", 14, 11)
movies.append(result)
print(movies)

result = purchase("thursday", "guardians of the galaxy", 15, 7)
movies.append(result)
print(movies)

week = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
week_list = []
for i in range(len(movies)):
    key = movies[i][0]
    week_list.append(key)

    print(week_list)
    if len(movies[i]) == 5 and movies[i][0] == key:
        list.append(movies[i][4])


tom = sum(list)
print(tom)
if tom > 20:
    print("you have bought too many tickets for this specific date")



#def purchase(movie, date, time, tickets):

from tkinter import *
import csv

# movies   name  tickets available   date   time

# MAKE SURE TO DO THE FILE.CLOSE THING WHEN SENDING THE STUFF in

movie_list = []
list = []


def purchase(date, movie, time, tickets):
    date_list = []

    def file_opening():
        file = open("ledger.csv", "r")

        reader = csv.reader(file, delimiter=',')

        for line in reader:
            movie_list.append(line)
        print(movie_list)
        file.close()
        return movie_list

    # watched = []
    movie_list.append(date)
    movie_list.append(movie)
    movie_list.append(time)
    movie_list.append(tickets)
    date_list.append(date)



    def ticket_check(tickets):
        file_opening()
        total = 0
        if tickets > 10:
            print("you cant buy that many tickets")
        else:
            movie_list.append(tickets)

    def more_checking(tickets, date):
        daily_tickets = []
        for i in range(len(date_list)):
            if date == date_list[i]:
                daily_tickets.append(tickets)
                print(daily_tickets)

    ticket_check(tickets)
    more_checking(tickets, date)
    return movie_list


result = purchase("wednesday", "star wars", 13, 14)
movie_list.append(result)
print(movie_list)

result = purchase("thursday", "batman", 14, 11)
movie_list.append(result)
print(movie_list)

result = purchase("thursday", "guardians of the galaxy", 15, 7)
movie_list.append(result)
print(movie_list)

for i in range(len(movie_list)):
    print(movie_list[i][4])



week = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
week_list = []
for i in range(len(movies)):
    key = movies[i][0]
    week_list.append(key)

    print(week_list)
    if len(movies[i]) == 5 and movies[i][0] == key:
        list.append(movies[i][4])

tom = sum(list)
print(tom)
if tom > 20:
    print("you have bought too many tickets for this specific date")



# def purchase(movie, date, time, tickets):




from tkinter import *
import csv

# movies   name  tickets available   date   time

# MAKE SURE TO DO THE FILE.CLOSE THING WHEN SENDING THE STUFF in

#print(file_opening())

def file_opening():

    file = open("ledger.csv", "r")
    movie_list = []
    reader = csv.reader(file, delimiter=',')
    for line in reader:
        movie_list.append(line)

    return movie_list

def purchase(date, movie, time, tickets):

    movie_list = file_opening()
    file = open("ledger.csv", 'w')

    if tickets <= 10:
        file.write(date + "," + movie + "," + time + "," + str(tickets))
        movie_list.append(date + "," + movie + "," + time + "," + str(tickets))
        print(movie_list)
        file.close()
        return("purchase confirmed"), movie_list

    if tickets > 10:
        return ("that is too many tickets"), movie_list


    def ticket_check(date, movie, time, tickets):
        total = 0
        for i in range(len(movie_list)):
            if movie_list[i][0] == date and movie_list[i][1] == movie and movie_list[i][2] == time:
                tickets += movie_list[i][3]
        if tickets > 10:
            print("too many tickets for this movie")
        return tickets


    def more_ticket_check(date, movie, time, tickets):
        daily_tickets = 0
        for i in range(len(movie_list)):
            if movie_list[i][0] == date:
                daily_tickets += movie_list[i][3]
            if daily_tickets > 20:
                print("too many tickets for this day")
        return daily_tickets

if __name__== "__main__":
    print(purchase("Wednesday", "star wars", "8:00", 7))



    def tickect_check():
        file_opening()
        total = 0
        print(movie_list)

        for i in range(len(movie_list)):
            if movie_list[i][1] == movie and movie_list[i][3] == time:
                total += movie_list[i][3]

            if total >10:
                print("reached limit")
        return total


    def more_ticket_check():
        file_opening()
        total_tickets = 0
        for i in range(len(movie_list)):
            if movie_list[i][0] == date:
                total_tickets += movie_list[i][3]
        return total_tickets


    total = tickect_check()
    daily = more_ticket_check()
    #file = open("ledger.csv")

def checking():
    if (total + tickets) <= 10 and (daily + tickets) <=20:
        file = open("ledger.csv", 'w')
        file.write(date + " " + movie + " " + time + " " + str(tickets) + "")
        file.close()
    if total + tickets >10:
        file = open("ledger.csv", 'r')
        file.close()
        return("purchaase denid")
    if daily + tickets >20:
        file = open("ledger.csv", 'r')
        file.close()
        return("purchase denied")

    print(tickect_check())
    print(more_ticket_check())

'''

import csv
def file_opening():
    file = open("ledger.csv", "r")
    movie_list = []

    reader = csv.reader(file, delimiter=',')
    for line in reader:
        movie_list.append(line)
    print(movie_list)
    return movie_list


def ticket_check(date, movie, time):
    movie_list = file_opening()
    total = 0
    try:
        for i in range(len(movie_list)):
            if movie_list[i][0] == date and movie_list[i][1] == movie and movie_list[i][2] == time:
                total += int(movie_list[i][3])
                if total > 10:
                    print("you bought too many tickets for this movie.")
    except:
        pass
    return total


def more_ticket_check(date, movie, time):
    movie_list = file_opening()
    daily_tickets = 0
    try:
        for i in range(len(movie_list)):
            print(movie_list[i][0], date)
            if movie_list[i][0] == date:
                daily_tickets += int(movie_list[i][3])
                if daily_tickets > 20:
                    print("you bought too many tickets for this day.")
    except Exception as exception:
        print(exception)
    return daily_tickets


def purchase(date, movie, time, tickets):
    movie_list = file_opening()
    #print(movie_list)
    file = open("ledger.csv", "a")
    daily_tickets = more_ticket_check(date, movie, time)
    total = ticket_check(date, movie, time)
    print(daily_tickets, total)
    if tickets + daily_tickets <= 10 and tickets + total <= 20:
        file.write(date + "," + movie + "," + time + "," + str(tickets) + "\n")

        file.close()
        return ("purchase confirmed")
        #return ("purchase confirmed")
    else:
        file.close()
        return("purchase denied")




if __name__== "__main__":
    purchase("5/19", "star wars", "7:00", 5)



