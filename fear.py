#This file will contain the methods dealing with users who want to look at
#fears.

#importing all libraries which will be used.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Importing files for use
from valid import *

class Fears():

    #This method will allow the user to select the activity that they want to see.
    def fear_selection(self, data):
        print("\033c")
        print("1. Flying")
        print("2. Storm")
        print("3. Darkness")
        print("4. Heights")
        print("5. Spiders")
        print("6. Snakes")
        print("7. Rats")
        print("8. Ageing")
        print("9. Speaking")
        choice = int(input("What do you want to look at: "))
        while not fear_valid(choice):
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
        plt.title("Fears", fontsize=24)
        plt.xlabel("Count", fontsize=14)
        plt.ylabel("Rating", fontsize=12)
        plt.show()
