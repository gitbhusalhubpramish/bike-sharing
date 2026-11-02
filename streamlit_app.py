import kagglehub
import pandas as pd
from sklearn.model_selection import train_test_split

path = kagglehub.dataset_download("yasserh/bike-sharing-dataset", "day.csv")

df = pd.read_csv(path)

x,y = df[["registered", "casual", "temp"]], df["cnt"]
xtrain,xtest,ytrain,ytest = train_test_split(x,y, random_state=42, test_size=0.2)
