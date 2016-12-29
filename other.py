#This file will contain the methods dealing with users who want to look at
#other.

#importing all libraries which will be used.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Importing files for use
from valid import *

class Others():

    #This method will allow the user to select the activity that they want to see.
    def other_selection(self, data):
        print("\033c")
        print("1. Appearence")
        print("2. Socializing")
        print("3. Finances")
        print("4. Malls")
        print("5. Name-Brand-Clothing")
        print("6. Entertainment Spending")
        print("7. Spending on Looks")
        print("8. Spending on Gadgets")
        print("9. spending on healthy Eating")
        choice = int(input("What do you want to look at: "))
        while not other_valid(choice):
            print("That was not a valid selection!")
            choice = int(input("What do you want to look at: "))
        if choice == 1:
            data = data[[44]]
            print(data)
            input("return")
        elif choice == 2:
            data = data[[45]]
        elif choice == 3:
            data = data[[46]]
        elif choice == 4:
            data = data[[47]]
        elif choice == 5:
            data = data[[48]]
        elif choice == 6:
            data = data[[49]]
        elif choice == 7:
            data = data[[50]]
        elif choice == 8:
            data = data[[51]]
        elif choice == 9:
            data = data[[52]]
        elif choice == 10:
            data = data[[53]]
        elif choice == 11:
            data = data[[54]]
