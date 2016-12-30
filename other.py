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
            data = data[[53]]
            print(data.mean())
            input("press enter to continue")
        elif choice == 2:
            data = data[[54]]
        elif choice == 3:
            data = data[[55]]
        elif choice == 4:
            data = data[[56]]
        elif choice == 5:
            data = data[[57]]
        elif choice == 6:
            data = data[[58]]
        elif choice == 7:
            data = data[[59]]
            print(data.mean())
            input("press enter to continue")
        elif choice == 8:
            data = data[[60]]
        elif choice == 9:
            data = data[[61]]
        elif choice == 10:
            data = data[[62]]
        elif choice == 11:
            data = data[[63]]

    #This method will graph the data.
    def graph(self, data):
        print("\033c")
        print("The graph will now be displayed")
        print("In order to move on, you must close the graph")
        input("Press Enter to continue ")
        count, rating = [], []
        count_value = 0
        while count_value < len(data):
            rating_value = data.iat[count_value, 0]
            rating.append(rating_value)
            count.append(count_value)
            count_value += 1
        plt.plot(count, rating, linewidth=2)
        plt.title("Other", fontsize=24)
        plt.xlabel("Count", fontsize=14)
        plt.ylabel("Rating", fontsize=12)
        plt.show()
