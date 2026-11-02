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

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(BASE_DIR, "forest.pkl")


class Node:
	def __init__(self, feature=None, treshold=None, left=None, right=None, value=None):
		self.feature=feature
		self.treshold= treshold
		self.left = left
		self.right = right
		self.value= value

with open("forest.pkl", "rb") as f:
	forest = pickle.load(f)
error = pd.read_csv("error.csv")

def build_graph(node):
	graph = []
	def traverse(node, node_id=0):
		nonlocal graph
		
		if node is None:
			return

		if node.value is not None:
			graph.append(f'{node_id} [label="predict: {node.value}"];')
			return
		graph.append(f'{node_id}[label="X[{node.feature}] <={node.treshold:.3f}"];')

		for child, child_id, label in [(node.left, 2*node_id+1, "True"), (node.right, 2*node_id+2, "False")]:

			if child:
				graph.append(f'{node_id}-> {child_id} [label="{label}"];')
				traverse(child,child_id)

	traverse(node)
	return "digraph Tree{" + "\n".join(graph) + "}"

st.graphviz_chart(build_graph(forest[-1][0]))
