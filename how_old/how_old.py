#!usr/bin/env python

"""
A function for telling the user how old they are, were, or will be on a given date.
"""

import datetime
import numpy as np 
import pandas as pd
import os.path
import random

def how_old(bday, endday):
    """
    returns the time elapsed since the inputted birthday in
    days.
    """
    age = endday - bday
    
    if endday==datetime.date.today():
        print("You are {} days old today!".format(age.days))

    elif endday > datetime.date.today():
        print("You will be {} days old on {}!".format(age.days, endday))

    elif endday < datetime.date.today():
        print ("You were {} days old on {}!".format(age.days, endday))

#import data for what_meal and what_random_meal
    
Days = pd.read_csv(os.path.abspath("hack-program/how_old/Days.csv"), index_col=0)
Months = pd.read_csv(os.path.abspath("hack-program/how_old/Months.csv"), index_col=0)
Year=pd.read_csv(os.path.abspath("hack-program/how_old/Year.csv"), index_col=0)    

def what_meal(bday):
    """
    returns a recipe suggestion based on the numerology of the date
    entered.
    """
    
    day=bday.day
    month=bday.month
    year=(bday.year % 10) + 1

    print ("Based on your birthday, you should eat {} with {} and {}.".format(Days.loc[day].values[0], 
    Months.loc[month].values[0], Year.loc[year].values[0]))

def what_random_meal():
    """
    returns a recipe suggestion based on nothing.
    """
    print("Based on random chance, you should eat {} with {} and {}.".format(Days.loc[random.randint(1,31)].values[0],
    Months.loc[random.randint(1,12)].values[0], Year.loc[random.randint(1,10)].values[0])) 

if __name__ == "__main__" :
    dayy= datetime.date.fromisoformat('1980-06-08')
    endyy=datetime.date.fromisoformat('2021-02-20')
    how_old(dayy, endyy)
    what_meal(dayy)
    what_random_meal()
    
