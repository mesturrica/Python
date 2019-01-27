import pandas as pd
import os

main_path = "Datasets/"
filepath = "titanic/titanic3.csv"

data = pd.read_csv(os.path.join(main_path, filepath))

# See null values, with values it turns an array, and with ravel, turn one line array.
print(pd.isnull(data["body"]).values.ravel().sum())

# Null values on a dataset can be caused by two reasons:
# - Problems with the data extraction
# - Data collection, can be caused by the data formats.

# Erase missing data
#print(data)
#print(data.dropna(axis=0, how="any"))

# Compute empty values
data2 = data
print(data2.fillna(0))

# Compute having in count the datatype
data2["body"] = data2["body"].fillna("Unknown")
print(data2)
#print(data2["body"].fillna("Unknown"))

# Put value of the most usual value of the column
data2["age"] = data2["age"].fillna(data["age"].mean())
print(data2["age"])
