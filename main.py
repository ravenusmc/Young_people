#importing all libraries which will be used.
import pandas as pd
import numpy as np

#Importing files for use
from valid import *
from music import *
from movies import *
from subjects import *
from activities import *

#This is the main function which will start the program.
def main():
    print("\033c")
    print("\t\t\t------------------------")
    print("\t\t\t-------Welcome to-------")
    print("\t\t\t----Young People Info---")
    print("\t\t\t------------------------")
    input("\t\t\tPress enter to continue ")
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
    print("Sex Selection:")
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
        print("\033c")
        print('You choose to look at data for males')
        print()
        print('There are', male_value, 'females', 'out of', total, 'people')
        print()
        input("Press enter to continue ")
        age_selection(data)
    elif option == 2:
        data = data[data.Gender == "female"]
        count = data.Gender.value_counts()
        female_value = count.iat[0]
        print("\033c")
        print('You choose to look at data for females')
        print()
        print('There are', female_value, 'females', 'out of', total, 'people')
        print()
        input("Press enter to continue ")
        age_selection(data)
    elif option == 3:
        age_selection(data)

#This function will allow the user to select what age range of the group that
#they are looking at.
def age_selection(data):
    print("\033c")
    print("Age selection screen")
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
    print("Please select where you want to see data from")
    print("1. Village")
    print("2. City")
    print("3. Both")
    option = int(input('What is your choice: '))
    while not valid_three(option):
        print("That is not a valid option")
        option = int(input("What is your choice? "))
    if option == 1:
        data = data[data.geography == "village"]
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
    print("2. Movies")
    print("3. School Subjects")
    print("4. Activities")
    option = int(input('What is your choice: '))
    #while not valid_choice(option):
    if option == 1:
        music = Music()
        music.music(data)
        music.graph(data)
    elif option == 2:
        movies = Movies()
        movies.movie_selection(data)
        movies.graph(data)
    elif option == 3:
        subject = Subjects()
        subject.subject_selection(data)
        subject.graph(data)
    elif option == 4:
        activity = Activities()
        activity.activity_selection(data)
        activity.graph(data)


main()
