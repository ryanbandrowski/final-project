# Wine Quality #

## Overview ##

The datasets are provided by [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Wine+Quality) 
and are made up of two datasets that are related to red and white variants of the Portuguese 
"Vinho Verde" wine. The datasets will be used to solve the following classification and regression 
tasks:
1. Predicting the quality of red wine (rating from 0 - 10).
2. Predicting the quality of white wine (rating from 0 - 10).
3. Predicting the type of wine (white or red).
4. Predicting the class quality of wine (both white and red; class quality -> poor, normal, 
excellent).

## Files and Folders ##
1. `dataset`: folder containing the wine datasets.
2. `prepare_dataset.ipynb`: this notebook converts the dataset into usable csv files to tackle the
specified tasks.
3. `predict_quality_red_wine.ipynb`: red wine quality prediction using regression analysis.
4. `predict_quality_red_wine_nn.ipynb`: red wine quality prediction using neural network.
5. `predict_quality_white_wine.ipynb`: white wine quality prediction using regression analysis.
6. `predict_quality_white_wine_nn.ipynb`: white wine quality prediction using neural network.
7. `predict_wine_type.ipynb`: predict the type of wine (white or red).
8. `predict_wine_type_nn.ipynb`: predict the type of wine (white or red) using neural network.

## Requirements ##
- Numpy
- Pandas
- Matplotlib
- Scikit-Learn
- Keras
- Seaborn
- Python