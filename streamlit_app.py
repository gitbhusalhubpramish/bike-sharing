import kagglehub
import pandas as pd
from sklearn.model_selection import train_test_split
import streamlit as st
import pickle
import json
import os

path = kagglehub.dataset_download("yasserh/bike-sharing-dataset", "day.csv")

df = pd.read_csv(path)

x,y = df[["registered", "casual", "temp"]], df["cnt"]
xtrain,xtest,ytrain,ytest = train_test_split(x,y, random_state=42, test_size=0.2)

st.write('''## Data(set)''')
st.write('''This project uses [bike sharing](https://www.kaggle.com/datasets/yasserh/bike-sharing-dataset) dataset in kaggle. This dataset contains the data of bike and it's sharing. The data is:''')
st.write('''- Total rows(data):''', len(df))
st.write('''- cnt(output) range:''', f"{min(y)} - {max(y)}")
st.write('''- Training sample''', len(xtrain))
st.write('''- Testing sample:''', len(xtest))

st.write('''## Algorithm''')
st.write('''This uses Random forest to predict the output(cnt the total bike rentals). Random forest trains many decision tree parellaly and return majyority bote or mean of the data. This is regression model''')

st.write('''## Model''')
st.write('''The visulization of forest of depth 10 is:''')

st.write([os.path.abspath(file) for file in os.listdir(".")])
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR,"forest.pkl"), "rb") as f:
	forest = json.load(f)
error = pd.read_csv("error.csv")

#st.write(os.listdir("."))
st.write(forest)
