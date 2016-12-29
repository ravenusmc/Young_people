#This file will contain the functions dealing with users who want to look at activities

#importing all libraries which will be used.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Importing files for use
from valid import *

class Activities():

    #This method will allow the user to select the activity that they want to see.
    def activity_selection(self, data):
        print("\033c")
        print("1. Cars")
        print("2. Art")
        print("3. Religion")
        print("4. Dancing")
        print("5. Music")
        print("6. Writing")
        print("7. Gardening")
        print("8. Shopping")
        print("9. Theatre")
        print("10. Friends")
        print("11. Pets")
        choice = int(input("What do you want to look at: "))
        while not activity_valid(choice):
            print("That was not a valid selection!")
            choice = int(input("What do you want to look at: "))
        if choice == 1:
            data = data[[33]]
        elif choice == 2:
            data = data[[34]]
        elif choice == 3:
            data = data[[35]]
        elif choice == 4:
            data = data[[36]]
        elif choice == 5:
            data = data[[37]]
        elif choice == 6:
            data = data[[38]]
        elif choice == 7:
            data = data[[39]]
        elif choice == 8:
            data = data[[40]]
        elif choice == 9:
            data = data[[41]]
        elif choice == 10:
            data = data[[42]]
        elif choice == 11:
            data = data[[43]]

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
        plt.title("Activities", fontsize=24)
        plt.xlabel("Count", fontsize=14)
        plt.ylabel("Rating", fontsize=12)
        plt.show()
