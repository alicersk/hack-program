#!usr/bin/env python

"""
Command line interface for how_old
"""

import argparse
import datetime

from how_old import how_old

def parse_command_line():
    "parses the arguments for the how_old function"

    #init parser and add arguments
    parser=argparse.ArgumentParser()

    parser.add_argument(
        'date',
        help="input the date of birth in ISO format: 'YYYY-MM-DD'", 
        type=str, 
        action="store"
    )

    args=parser.parse_args()

    return args     

def main():
    "run the function with the parsed arguments"

    args = parse_command_line()

    how_old(datetime.date.fromisoformat(args.date))


if __name__ =="__main__":
  
    how_old(datetime.date.fromisoformat('2020-02-08'))
