# Bike-sharing dataset with Random-forest

In this project I have applied Random forest from scratch in [Bike-sharing](https://www.kaggle.com/datasets/yasserh/bike-sharing-dataset) dataset in kaggle from it's notebook, trained it, stored the parameter and show the preview in streamlit app. This markdown is just the preview of the project and how I made this. I have given more details in my [notes](https://github.com/gitbhusalhubpramish/ml-notes/tree/main/0.005%20random-forest) about random forest.

<img src="visual.svg"/>

This is what a decision tree looks like. random forest is the collection of trees like this. I have rendered 20 tree of depth 10 like this in [preview](https://bike-sharing-dataset-random-forest.streamlit.app/).

## Small intro to Random forest

Random forest is a supervised meachine learning algorithm where it runs many decision tree parallely in different data and take majyority votes or mean as output. This can be classification or regression. I've used regression model.

## Feature

This project was made by me to understand Random forest form scratch so it has random forest applied from scratch - trainied in kaggle notebooks and preview in streamlit app. But also:

- Random forest from scratch
- decision tree visulization
- GPU Parellized processing

## Tech-Stack

This project uses python liberies used for data science - Visulization, calculation and data manipulation. I've used:

- Numpy for calculation
- Streamlit for data visulizaion and preview
- cupy for GPU bahsed parellel processing
- Pandas for data manipulaion
- sk-learn for datasplit.
- Graphviz for graph visulization


