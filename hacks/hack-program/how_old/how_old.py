#!usr/bin/env python

"""
A function for telling the user how old they are in days, weeks or years.
"""

import datetime

def how_old(bday):
    """
    returns the time elapsed since the inputted birthday in
    days.
    """
    age = datetime.date.today() - bday
    
    print("You are {} days old today!".format(age.days))
    
if __name__ == "__main__" :
    dayy= datetime.date.fromisoformat('2020-02-08')
    
    how_old(dayy)

    

    
