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
            data = data[[21]]
        if choice == 2:
            data = data[[22]]
        if choice == 3:
            data = data[[23]]
        if choice == 4:
            data = data[[24]]
