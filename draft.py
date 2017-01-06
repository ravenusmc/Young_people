#importing all libraries which will be used.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import collections

# prac = {}
# prac['topic'] = 'Horror'
# print(prac)

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
    values.append(format(value, '.2f'))
    count += 1
mean_count = 0
topic_mean_dict = {}
for topic in topics:
    topic_mean_dict[topic] = values[mean_count]
    mean_count += 1
sorted_dict = sorted([(value,key) for (key,value) in topic_mean_dict.items()], reverse=True)
count_value = 0
for item in sorted_dict:
    value = sorted_dict[count_value]
    # print(low[0])
    print('The mean for', value[1], 'is the following:', value[0])
    count_value += 1
max_value = max(values)
location_max_value = values.index(max_value)
# print()
# print('The max value is', format(max_value, '.2f'), 'which is', topics[location_max_value])
# print()

# worst = sorted([(value,key) for (key,value) in topic_mean_dict.items()], reverse=True)
# count = 0
# for item in worst:
#     low = worst[count]
#     # print(low[0])
#     print('The mean for', low[1], 'is the following:', low[0])
#     count += 1

# low = worst[0]
# print(low[1])
# for key in topic_mean_dict:
#     print('The mean for', key, 'is the following:', topic_mean_dict[key])
