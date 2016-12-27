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
