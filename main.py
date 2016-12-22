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

#This function will get the total number of individuals who did the survey
def get_total(data):
    count = data.Gender.value_counts()
    female_count = count.iat[0]
    male_count = count.iat[1]
    total_count = female_count + male_count
    return total_count

#This is the main menu function.
def sex_selection():
    print("\033c")
    #Pulling in the data from the csv.
    data = pd.read_csv('responses.csv')
    total = get_total(data)
    print("1. Look at data for males")
    print("2. Look at data for females")
    print("3. Look at data for both males and females")
    option = int(input("What is your choice? "))
    #Validation loop
    while not valid_three(option):
        print("That is not a valid option")
        option = int(input("What is your choice? "))
    if option == 1:
        data = data[data.Gender == "male"]
        count = data.Gender.value_counts()
        male_value = count.iat[0]
        print('You choose to look at data for males')
        print('Out of', total, 'people there are', male_value, 'males.')
        input("Press enter to continue ")
        age_selection(data)
    elif option == 2:
        data = data[data.Gender == "female"]
        count = data.Gender.value_counts()
        female_value = count.iat[0]
        print('You choose to look at data for females')
        print('Out of', total, 'people there are', female_value, 'females.')
        input("Press enter to continue ")
        age_selection(data)
    elif option == 3:
        age_selection(data)

#This function will allow the user to select what age range of the group that
#they are looking at.
def age_selection(data):
    print("\033c")
    age = int(input("Please enter an age that you want to look at: "))
    while not age_validation(age):
        print("That is not an acceptable age")
        age = int(input("Please enter an age that you want to look at: "))
    data = data[data.Age >= age]
    geography(data)

#This function will let the user decide if they want to look at people
#in the country, city or both
def geography(data):
    print("\033c")
    print("1. Village")
    print("2. City")
    print("3. Both")
    option = int(input('What is your choice: '))
    while not valid_three(option):
        print("That is not a valid option")
        option = int(input("What is your choice? "))
    if option == 1:
        data = data[data.geography == "village"]
        print(data.head())
        input("Press enter to continue ")
        choose_topic(data)
    elif option == 2:
        data = data[data.geography == "city"]
        choose_topic(data)
    elif option == 3:
        choose_topic(data)

#This function will allow the user to choose which topic they want to
#zoom in on.
def choose_topic(data):
    print("\033c")
    print("1. Music")
    print("2. Spending")
    option = int(input('What is your choice: '))

main()
