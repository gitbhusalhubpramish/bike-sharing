import kagglehub
import pandas as pd
from sklearn.model_selection import train_test_split
import streamlit as st

path = kagglehub.dataset_download("yasserh/bike-sharing-dataset", "day.csv")

df = pd.read_csv(path)

x,y = df[["registered", "casual", "temp"]], df["cnt"]
xtrain,xtest,ytrain,ytest = train_test_split(x,y, random_state=42, test_size=0.2)

st.write('''## Data(set)''')
st.write('''This project uses [bike sharing] dataset in kaggle. This dataset contains the data of bike and it's sharing. The data is:''')
st.write('''- Total rows(data):''', len(df))
st.write('''- cnt(output) range''', f"{min(y)} - {max(y)}")
