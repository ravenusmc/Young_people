#importing all libraries which will be used.
import pandas as pd
import numpy as np

#Importing files for use
from valid import *

#This is the main function which will start the program.
def main():
    print("\033c")
    print("------------------------")
    print("-------Welcome to-------")
    print("----Young People Info---")
    print("------------------------")
    input("Press enter to continue ")
    sex_selection()


#This is the main menu function.
def sex_selection():
    print("\033c")
    #Pulling in the data from the csv.
    data = pd.read_csv('responses.csv')
    print("1. Look at data for males")
    print("2. Look at data for females")
    print("3. Look at data for both males and females")
    option = int(input("What is your choice? "))
    #Validation loop
    while not sex_selection_valid(option):
        print("That is not a valid option")
        option = int(input("What is your choice? "))
    if option == 1:
        data = data[data.Gender == "male"]
        geography(data)
    elif option == 2:
        data = data[data.Gender == "female"]
        geography(data)
    elif option == 3:
        geography(data)

def geography(data):
    print("\033c")
    print("1. Village")
    print("2. City")

main()
