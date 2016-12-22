#This file will contain the functions dealing with users who want to look at music 

#Importing files for use
from valid import *

def music(data):
  print("\033c")
  print("1. Country")
  print("2. Classical")
  print("3. Pop")
  print("4. Rock")
  print("5. Punk")
  print("6. HipHop")
  print("7. Swing")
  print("8. Rock")
  print("9. Alternative")
  print("10. Techno")
  choice = int(input("What do you want to look at: "))
  while not music_valid(choice):
    print("That is not a valid selection")
    choice = int(input("What do you want to look at: "))
  if choice == 1:
    data = data[data.Country]
    print(data.head())