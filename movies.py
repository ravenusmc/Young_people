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
        print("4. Romantic")
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
            data = data[[9]]
            #This line I use to remove all of the NaN values.
            data = data[np.isfinite(data['Horror'])]
        elif choice == 2:
            data = data[[10]]
            data = data[np.isfinite(data['Thriller'])]
        elif choice == 3:
            data = data[[11]]
            data = data[np.isfinite(data['Comedy'])]
        elif choice == 4:
            data = data[[12]]
            data = data[np.isfinite(data['Romantic'])]
        elif choice == 5:
            data = data[[13]]
            data = data[np.isfinite(data['Sci-fi'])]
        elif choice == 6:
            data = data[[14]]
            data = data[np.isfinite(data['War'])]
        elif choice == 7:
            data = data[[15]]
            data = data[np.isfinite(data['Fantasy'])]
        elif choice == 8:
            data = data[[16]]
            data = data[np.isfinite(data['Animated'])]
        elif choice == 9:
            data = data[[17]]
            data = data[np.isfinite(data['Documentary'])]
        elif choice == 10:
            data = data[[18]]
            data = data[np.isfinite(data['Western'])]
        elif choice == 11:
            data = data[[19]]
            data = data[np.isfinite(data['Action'])]

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
        plt.title("Movies", fontsize=24)
        plt.xlabel("Count", fontsize=14)
        plt.ylabel("Rating", fontsize=12)
        plt.show()

    #This method will show the user the mean of each topic within
    #each category.
    def show_mean(self, data):
        print("\033c")
        #I set up a list holding all of the topics within the category
        topics = ['Horror', 'Thriller', 'Comedy', 'Romantic', 'Sci-fi', 'War', 'Fantasy', 'Animated', 'Documentary', 'Western', 'Action']
        count = 9
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
        graph_data = mean[['Horror', 'Thriller', 'Comedy', 'Romantic', 'Sci-fi', 'War', 'Fantasy', 'Animated', 'Documentary', 'Western', 'Action']].plot(kind='bar', title ="Music", figsize=(10, 9), legend=True, fontsize=12)
        graph_data.set_xlabel("Movie Type", fontsize=12)
        graph_data.set_ylabel("Rating", fontsize=12)
        plt.show()
