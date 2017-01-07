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
            data = data[[32]]
            #This line I use to remove all of the NaN values.
            data = data[np.isfinite(data['Cars'])]
        elif choice == 2:
            data = data[[33]]
            data = data[np.isfinite(data['Art'])]
        elif choice == 3:
            data = data[[34]]
            data = data[np.isfinite(data['Religion'])]
        elif choice == 4:
            data = data[[35]]
            data = data[np.isfinite(data['Dancing'])]
        elif choice == 5:
            data = data[[36]]
            data = data[np.isfinite(data['Music'])]
        elif choice == 6:
            data = data[[37]]
            data = data[np.isfinite(data['Writing'])]
        elif choice == 7:
            data = data[[38]]
            data = data[np.isfinite(data['Gardening'])]
        elif choice == 8:
            data = data[[39]]
            data = data[np.isfinite(data['Shopping'])]
        elif choice == 9:
            data = data[[40]]
            data = data[np.isfinite(data['Theatre'])]
        elif choice == 10:
            data = data[[41]]
            data = data[np.isfinite(data['Friends'])]
        elif choice == 11:
            data = data[[42]]
            data = data[np.isfinite(data['Pets'])]

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
        plt.title("Activities", fontsize=24)
        plt.xlabel("Count", fontsize=14)
        plt.ylabel("Rating", fontsize=12)
        plt.show()

    #This method will show the user the mean of each topic within
    #each category.
    def show_mean(self, data):
        print("\033c")
        #I set up a list holding all of the topics within the category
        topics = ['Cars', 'Art', 'Religion', 'Dancing', 'Music', 'Writing', 'Gardening', 'Shopping','Theatre', 'Friends', 'Pets']
        count = 32
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
        graph_data = mean[['Cars', 'Art', 'Religion', 'Dancing', 'Music', 'Writing', 'Gardening', 'Shopping','Theatre', 'Friends', 'Pets']].plot(kind='bar', title ="Music", figsize=(10, 9), legend=True, fontsize=12)
        graph_data.set_xlabel("Activity Type", fontsize=12)
        graph_data.set_ylabel("Rating", fontsize=12)
        plt.show()
