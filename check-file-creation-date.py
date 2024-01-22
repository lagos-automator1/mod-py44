#! /usr/bin/python3
## Checks creation date of specified file


import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    print(os.name)

    user_input = str(input("Welcome to PhunkyTech's file checker\nType name of file to check: "))
    t = time.ctime(path.getmtime(user_input))
    print("This file was created on ", t)


if __name__ == "__main__":
    main()
