#!usr/bin/env python

"""
Command line interface for how_old
"""

import argparse
import datetime

from how_old import how_old, what_meal, what_random_meal

def parse_command_line():
    "parses the arguments for the how_old module"

    #init parser and add arguments
    parser=argparse.ArgumentParser()

    parser.add_argument(
        'date',
        help="input the date of birth in ISO format: 'YYYY-MM-DD'", 
        type=str, 
        action="store"
    )
    parser.add_argument(
       'enddate',
       help= "input the date on which you want to know your age in ISO format: 'YYYY-MM-DD'",
       default= "-today",
       type=str,
       action="store"
    )
    parser.add_argument(
        '--meal',
        help="get a suggestion on a meal you would like based on numerology",
        action="store_true", 
        default=False
    )
    parser.add_argument(
        '--random',
        help="recommends a random meal: warning, this meal may not be numerologically appropriate",
        action="store_true",
        default=False
    )
    args=parser.parse_args()

    return args     

def main():
    "run the function with the parsed arguments"
    args = parse_command_line()
    
    how_old(datetime.date.fromisoformat(args.date), datetime.date.fromisoformat(args.enddate))

    if args.meal == True:
        what_meal(datetime.date.fromisoformat(args.date))

    if args.random == True:
        what_random_meal()    

if __name__ =="__main__":
  
    how_old(datetime.date.fromisoformat('2020-02-08'), datetime.date.fromisoformat('1980-01-02'))
    what_random_meal()