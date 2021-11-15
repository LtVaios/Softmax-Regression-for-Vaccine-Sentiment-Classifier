import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.feature_extraction.text import *

trainset = pd.read_csv("./vs_train.csv")
testset = pd.read_csv("./vs_dev.csv")
trainset.head()
trainset.describe()
print(1)




