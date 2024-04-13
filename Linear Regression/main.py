import pandas as pd 
import  numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


url = ""
dataset = pd.read_csv(url)

dataset.plot(x='MinTemp', y='MaxTemp',style='o')
plt.title('Min & Max Temp')
plt.xlabel("Mintemp")
plt.ylabel("Maxtemp")
plt.show()