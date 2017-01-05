#importing all libraries which will be used.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('responses.csv')
#print(data.head())
data = data[data.Gender == "male"]
data = data[data.Age >= 20]
data = data[data.geography == "city"]
topics = ['Horror', 'Thriller', 'Comedy', 'Romantic', 'Sci-fi', 'War', 'Fantasy', 'Animated', 'Documentary', 'Western', 'Action', 'History']
count = 10
values = []
mean = data.mean()
for topic in topics:
    value = mean[count]
    values.append(value)
    count += 1
mean_count = 0
for topic in topics:
    print('The mean for', topic, 'is the following:', format(values[mean_count], '.2f'))
    mean_count += 1
max_value = max(values)
location_max_value = values.index(max_value)
print()
print('The max value is', format(max_value, '.2f'), 'which is', topics[location_max_value])
print()


# mean = mean[0]
# print("The mean is ", mean)

# count = 0
# topics = ['Country', 'Classical', 'Pop', 'Rock', 'Punk', 'Hiphop', 'Swing', 'Rock', 'Alternative', 'Techno']
# while count < 9:
#     data = data[[count]]
#     print(data.head())
#     count += 1


# topics = ['Country', 'Classical', 'Pop', 'Rock', 'Punk', 'Hiphop', 'Swing', 'Rock', 'Alternative', 'Techno']
# # count = 0
# for topic in topics:
# #     data = data[[count]]
# #     print(data)
#     data = data[np.isfinite(data[topic])]
#     mean = data.mean()
#     mean = mean[0]
#     print(mean)
    #count += 1




# data = data.mean()
# mean = data[0]
# print(mean)
#print(data.iat[4,0])

# count, rating = [], []
# count_value = 0
# while count_value < len(data):
#     rating_value = data.iat[count_value, 0]
#     rating.append(rating_value)
#     count.append(count_value)
#     count_value += 1
#
# rating = sorted(rating, reverse=True)
#
# plt.plot(count, rating, linewidth=2)
# plt.title("Graph", fontsize=24)
# plt.xlabel("Count", fontsize=14)
# plt.ylabel("Rating", fontsize=12)
# plt.show()
