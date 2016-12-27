#This file will contain the functions dealing with users who want to look at movies

#importing all libraries which will be used.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Importing files for use
from valid import *

#This class will hold all of the movie functions.
class Movies():

    def movie_selection(self, data):
        print("\033c")
        print("1. Horror")
        print("2. Thriller")
        print("3. Comedy")
        print("4. Romatic")
        print("5. Sci-fi")
        print("6. War")
        print("7. Fantasy")
        print("8. Animated")
        print("9. Documentary")
        print("10. Western")
        print("11. Action")
        choice = int(input("What do you want to look at: "))
        while not movie_valid(choice):
            print("That selection is not allowed")
            choice = int(input("What do you want to look at: "))
        if choice == 1:
            data = data[[10]]
        elif choice == 2:
            data = data[[11]]
        elif choice == 3:
            data = data[[12]]
        elif choice == 4:
            data = data[[13]]
        elif choice == 5:
            data = data[[14]]
        elif choice == 6:
            data = data[[15]]
        elif choice == 7:
            data = data[[16]]
        elif choice == 8:
            data = data[[17]]
        elif choice == 9:
            data = data[[18]]
        elif choice == 10:
            data = data[[19]]
        elif choice == 11:
            data = data[[20]]
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
        plt.title("Movies", fontsize=24)
        plt.xlabel("Count", fontsize=14)
        plt.ylabel("Rating", fontsize=12)
        plt.show()
