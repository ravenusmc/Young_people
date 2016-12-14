#importing all libraries which will be used.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('responses.csv')
#print(data.head())
data = data[data.Gender == "male"]
count = data.Gender.value_counts()
value = count.iat[0]
print(value)


#print(data.count(axis=0, level=None, numeric_only=False))
