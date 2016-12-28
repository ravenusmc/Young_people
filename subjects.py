#This file will contain the functions dealing with users who want to look at School Subjects

#importing all libraries which will be used.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Importing files for use
from valid import *

class Subjects():

    def subject_selection(self, data):
        print("\033c")
        print("1. History")
        print("2. Psychology")
        print("3. Politics")
        print("4. Math")
        print("5. Physics")
        print("6. Biology")
        print("7. Chemistry")
        print("8. Reading")
        print("9. Geography")
        print("10. Languages")
        print("11. Medicine")
        print("12. Law")
        choice = int(input("What do you want to look at: "))
        while not subjects_valid(choice):
            print("That was not a valid selection!")
            choice = int(input("What do you want to look at: "))
        if choice == 1:
            data = data[[21]]
        elif choice == 2:
            data = data[[22]]
        elif choice == 3:
            data = data[[23]]
        elif choice == 4:
            data = data[[24]]
        elif choice == 5:
            data = data[[25]]
        elif choice == 6:
            data = data[[26]]
        elif choice == 7:
            data = data[[27]]
        elif choice == 8:
            data = data[[28]]
        elif choice == 9:
            data = data[[29]]
        elif choice == 10:
            data = data[[30]]
        elif choice == 11:
            data = data[[31]]
        elif choice == 12:
            data = data[[32]]
            print(data)

    #This function will graph the data.
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
        plt.title("School Subjects", fontsize=24)
        plt.xlabel("Count", fontsize=14)
        plt.ylabel("Rating", fontsize=12)
        plt.show()
