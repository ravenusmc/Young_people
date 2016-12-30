#Importing files for use
from valid import *

#This class will hold functions that help to run the program.
class Info():

    def main_menu(self):
        print("\033c")
        print("1. Use Program")
        print("2. Background Information")
        choice = int(input("What is your choice? "))
        while not main_menu_valid(choice):
            print("That is not a proper selection")
            choice = int(input("What is your choice? "))
        if choice == 1:
            print("You will not be heading to choose sex")
            input("Press enter to continue ")
        elif choice == 2:
            info = Info()
            info.background()

    def background(self):
        print("\033c")
        print("\t\t\tBasic Information:")
        print("""
        This program looks at how much people like or dislike a specific
        topic. The user will be able to look at topics such as fears, school
        subjects, movie genre's etc and see how much individuals like those
        topics. A value closer to 1 means it is not well liked while a
        value closer to 5 means it is well liked. There is some more
        information located at the readme file.
        """ )
        input("\t\t\t press enter to continue ")
