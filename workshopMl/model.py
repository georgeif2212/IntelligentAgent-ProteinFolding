import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt


# * load dataset
df = pd.read_csv("ObesityDataSet.csv")

# * show first rows
print("Dataset dimensions:", df.shape)
print("\First 5rows:")
print(df.head())

# * show data types
print("\nData types:")
print(df.dtypes)

# * Show unique values per column
print("\nUnique values per categoric variable:")
for col in df.columns:
    if df[col].dtype == "object":
        print(f"{col}: {df[col].unique()}")
