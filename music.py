#This file will contain the functions dealing with users who want to look at music
#importing all libraries which will be used.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Importing files for use
from valid import *

#This function will allow the user to select which aspect of music
#that the user wants to see.
def music(data):
    print("\033c")
    print("1. Country")
    print("2. Classical")
    print("3. Pop")
    print("4. Rock")
    print("5. Punk")
    print("6. HipHop")
    print("7. Swing")
    print("8. Rock")
    print("9. Alternative")
    print("10. Techno")
    choice = int(input("What do you want to look at: "))
    while not music_valid(choice):
        print("That is not a valid selection")
        choice = int(input("What do you want to look at: "))
    if choice == 1:
        data = data[[0]]
        graph(data)

#This function will graph the data.
def graph(data):
    print("\033c")
    print("The graph will now be displayed")
    input("Press Enter to continue ")
    count, rating = [], []
    count_value = 0
    while count_value < len(data):
        rating_value = data.iat[count_value, 0]
        rating.append(rating_value)
        count.append(count_value)
        count_value += 1
    plt.plot(count, rating, linewidth=2)
    plt.title("Country Music", fontsize=24)
    plt.xlabel("Count", fontsize=14)
    plt.ylabel("Rating", fontsize=12)
    plt.show()
