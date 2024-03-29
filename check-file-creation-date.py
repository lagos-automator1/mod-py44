#! /usr/bin/python3
## Checks creation date of specified file


import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    print(os.name)
    
    # Gets user input - value of file to check
    user_input = str(input("Welcome to PhunkyTech's file checker\nType name of file to check: "))
    # get the modification time of the file using path module
    # then convert to readable time using the time class's ctime function
    t = time.ctime(path.getmtime(user_input))
    print("This file was created on ", t)
    # constructs datetime object using get modification time function(getmtime)
    print (datetime.datetime.fromtimestamp(path.getmtime(user_input)))

    # calculate how long ago the item was modified
    mod_date = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime(user_input))
    print("This file hasn't been touched since ", mod_date, "ago.")
    print("Or,", mod_date.total_seconds(),"seconds")


if __name__ == "__main__":
    main()
