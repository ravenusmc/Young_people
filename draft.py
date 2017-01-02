#importing all libraries which will be used.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('responses.csv')
#print(data.head())

data = data[data.Gender == "female"]
data = data[data.geography == "city"]
data = data[[52]]
data = data[np.isfinite(data['Speaking'])]

# data = data.mean()
# mean = data[0]
# print(mean)
#print(data.iat[4,0])

count, rating = [], []
count_value = 0
while count_value < len(data):
    rating_value = data.iat[count_value, 0]
    rating.append(rating_value)
    count.append(count_value)
    count_value += 1

rating = sorted(rating, reverse=True)
print(rating)

plt.plot(count, rating, linewidth=2)
plt.title("Graph", fontsize=24)
plt.xlabel("Count", fontsize=14)
plt.ylabel("Rating", fontsize=12)
plt.show()
