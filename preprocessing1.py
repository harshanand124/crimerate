import customtkinter as ctk
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

data = pd.read_csv('new_datasetcsv.csv')

df = pd.DataFrame(data)

categorical_cols = ['City', 'Type']
numeric_cols = ['Year', 'Population']
target_col = 'Crime Rate'

preprocessor = ColumnTransformer(transformers=[('cat', OneHotEncoder(), categorical_cols)],remainder='passthrough')

model = Pipeline(steps=[('preprocessor', preprocessor),('regressor', LinearRegression())])

X = df[categorical_cols + numeric_cols]
y = df[target_col]

model.fit(X, y)
