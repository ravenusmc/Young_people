#This file will contain the functions dealing with users who want to look at music
#importing all libraries which will be used.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Importing files for use
from valid import *

#This class will hold all of the music functions.
class Music():

#This function will allow the user to select which aspect of music
#that the user wants to see.
    def music(self, data):
        print("\033c")
        print("1. Country")
        print("2. Classical")
        print("3. Pop")
        print("4. Rock")
        print("5. Punk")
        print("6. HipHop")
        print("7. Swing")
        print("8. Alternative")
        print("9. Techno")
        choice = int(input("What do you want to look at: "))
        while not music_valid(choice):
            print("That is not a valid selection")
            choice = int(input("What do you want to look at: "))
        if choice == 1:
            data = data[[0]]
            #This line I use to remove all of the NaN values.
            data = data[np.isfinite(data['Country'])]
        elif choice == 2:
            data = data[[1]]
            data = data[np.isfinite(data['Classical'])]
        elif choice == 3:
            data = data[[2]]
            data = data[np.isfinite(data['Pop'])]
        elif choice == 4:
            data = data[[3]]
            data = data[np.isfinite(data['Rock'])]
        elif choice == 5:
            data = data[[4]]
            data = data[np.isfinite(data['Punk'])]
        elif choice == 6:
            data = data[[5]]
            data = data[np.isfinite(data['Hiphop'])]
        elif choice == 7:
            data = data[[6]]
            data = data[np.isfinite(data['Swing'])]
        elif choice == 8:
            data = data[[7]]
            data = data[np.isfinite(data['Alternative'])]
        elif choice == 9:
            data = data[[8]]
            data = data[np.isfinite(data['Techno'])]


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
        rating = sorted(rating, reverse=True)
        plt.plot(count, rating, linewidth=2)
        plt.title("Music", fontsize=24)
        plt.xlabel("Count", fontsize=14)
        plt.ylabel("Rating", fontsize=12)
        plt.show()

    #This method will show the user the mean of each topic within
    #each category.
    def show_mean(self, data):
        print("\033c")
        #I set up a list holding all of the topics within the category
        topics = ['Country', 'Classical', 'Pop', 'Rock', 'Punk', 'Hiphop', 'Swing', 'Alternative', 'Techno']
        count = 0
        #This list will hold all of the mean values for each topic.
        values = []
        #This mean variable will hold all of the mean values
        mean = data.mean()
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
        ax = mean[['Country', 'Classical', 'Pop', 'Rock', 'Punk', 'Hiphop', 'Swing', 'Alternative', 'Techno']].plot(kind='bar', title ="Music", figsize=(10, 9), legend=True, fontsize=12)
        ax.set_xlabel("Music Type", fontsize=12)
        ax.set_ylabel("Rating", fontsize=12)
        plt.show()
