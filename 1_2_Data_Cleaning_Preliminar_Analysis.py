import pandas as pd
import os

main_path = "Datasets/"
filepath = "titanic/titanic3.csv"

data = pd.read_csv(os.path.join(main_path, filepath))

# Test if we're reading the data in the correct way.
print(data.head())

# Function to see the number of rows and columns of the file, it's called 'dimension'
print(data.shape)

# Function to see the headers of the columns we have load in the dataset
print(data.columns.values)

# Summary of the numeric variables
print(data.describe())

# To see the data type of every column
print(data.dtypes)