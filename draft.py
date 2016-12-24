#importing all libraries which will be used.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('responses.csv')
#print(data.head())

data = data[data.Gender == "female"]
data = data[data.geography == "city"]
data = data[[0]]
# print(data)
# print(data.mean())
print(len(data))
#print(data.head())
#print("The graph will now be displayed")
#input("Press Enter to continue")
count, rating = [], []
count_value = 0
#print(data.iat[4,0])
while count_value < len(data):
    rating_value = data.iat[count_value, 0]
    rating.append(rating_value)
    count.append(count_value)
    count_value += 1
plt.plot(count, rating, linewidth=2)
plt.title("Country Music", fontsize=24)
plt.xlabel("Count", fontsize=14)
plt.ylabel("Rating", fontsize=12)
plt.show()


#test = ufo[ufo.Time.str.contains(value)]
#date.append(value)
#number = test.City.count()
#year.append(int(number))
#newValue = int(value)
#newValue += 1
#value = str(newValue)
#count += 1
