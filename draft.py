#importing all libraries which will be used.
import pandas as pd
import numpy as np


data = pd.read_csv('responses.csv')

#print(data.head())

test = data[data.Gender == "female"]
testTwo = test[test.handed == "right handed"]
print(testTwo)
