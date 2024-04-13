import pandas as pd 
import  numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


url = ""
dataset = pd.read_csv(url)

dataset.plot(x='skill1', y='skill2',style='o')
plt.title('Skill 1 & Skill2')
plt.xlabel("Skill1")
plt.ylabel("Skill2")
plt.show()