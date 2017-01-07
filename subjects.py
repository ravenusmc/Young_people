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
            data = data[[20]]
            #This line I use to remove all of the NaN values.
            data = data[np.isfinite(data['History'])]
        elif choice == 2:
            data = data[[21]]
            data = data[np.isfinite(data['Psychology'])]
        elif choice == 3:
            data = data[[22]]
            data = data[np.isfinite(data['Politics'])]
        elif choice == 4:
            data = data[[23]]
            data = data[np.isfinite(data['Math'])]
        elif choice == 5:
            data = data[[24]]
            data = data[np.isfinite(data['Physics'])]
        elif choice == 6:
            data = data[[25]]
            data = data[np.isfinite(data['Biology'])]
        elif choice == 7:
            data = data[[26]]
            data = data[np.isfinite(data['Chemistry'])]
        elif choice == 8:
            data = data[[27]]
            data = data[np.isfinite(data['Reading'])]
        elif choice == 9:
            data = data[[28]]
            data = data[np.isfinite(data['Geography'])]
        elif choice == 10:
            data = data[[29]]
            data = data[np.isfinite(data['Languages'])]
        elif choice == 11:
            data = data[[30]]
            data = data[np.isfinite(data['Medicine'])]
        elif choice == 12:
            data = data[[31]]
            data = data[np.isfinite(data['Law'])]

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
        rating = sorted(rating, reverse=True)
        plt.plot(count, rating, linewidth=2)
        plt.title("School Subjects", fontsize=24)
        plt.xlabel("Count", fontsize=14)
        plt.ylabel("Rating", fontsize=12)
        plt.show()

    #This method will show the user the mean of each topic within
    #each category.
    def show_mean(self, data):
        print("\033c")
        #I set up a list holding all of the topics within the category
        topics = ['History', 'Psychology', 'Politics', 'Math', 'Physics', 'Biology', 'Chemistry', 'Reading','Geography', 'Languages', 'Medicine', 'Law']
        count = 20
        #This list will hold all of the mean values for each topic.
        values = []
        #data = data[np.isfinite(data['Horror'])]
        #This mean variable will hold all of the mean values
        mean = data.mean()
        #I have to use this for loop instead of a while one to ensure that I go through
        #each value in the list. Count will have a different starting point for each
        #category so working with the length of the list will not work when the
        #count is above 10
        for topic in topics:
            #This variable gets the specific value of a mean in the list
            value = mean[count]
            #The value variable, holding a speficic mean, is then appended to a list
            values.append(format(value, '.2f'))
            count += 1
        mean_count = 0
        #Here I am setting up a dictionary to combine the mean with its topic
        topic_mean_dict = {}
        #I loop through the topics list to combine a topic with its mean
        for topic in topics:
            topic_mean_dict[topic] = values[mean_count]
            mean_count += 1
        #This variable will hold the new variable of my sorted dicitionary list.
        sorted_dict = sorted([(value,key) for (key,value) in topic_mean_dict.items()], reverse=True)
        count_value = 0
        #I then iterate again through the topics list to show the user where all the values are.
        for item in sorted_dict:
            value = sorted_dict[count_value]
            print('The mean for', value[1], 'is the following:', value[0])
            count_value += 1
        #Creating a variable to hold the max value.
        max_value = max(values)
        #Creating a variable to hold the location of a max value
        location_max_value = values.index(max_value)
        print()
        print('The max value is', max_value, 'which is', topics[location_max_value])
        print()
        input("Press Enter to continue ")
        return mean

    #This method will allow the user to see graphs of the mean values.
    def graph_of_means(self, data, mean):
        print("\033c")
        print("The graph will now be displayed")
        print("In order to move on, you must close the graph")
        input("Press Enter to continue ")
        graph_data = mean[['History', 'Psychology', 'Politics', 'Math', 'Physics', 'Biology', 'Chemistry', 'Reading','Geography', 'Languages', 'Medicine', 'Law']].plot(kind='bar', title ="Music", figsize=(10, 9), legend=True, fontsize=12)
        graph_data.set_xlabel("Subject Type", fontsize=12)
        graph_data.set_ylabel("Rating", fontsize=12)
        plt.show()
