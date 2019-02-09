import pandas as pd

# First, we read a local csv
data = pd.read_csv('../Datasets/customer-churn-model/Customer Churn Model.txt')

# We print data to see that we're loading correctly.
print(data.head())

# Get n rows of data (First value included, last one not)
data_subset = data[1:3]

print(data_subset.head())

# Users with Day Mins > 50
data1 = data[data["Day Mins"]>50]
print(data1.head())

# Users of NY
data2 = data[data["State"] == "NY"]
print(data2)

# AND
data3 = data[(data["Day Mins"]>300) & (data["State"]=="NY")]
print(data3)

# OR
data4 = data[(data["Day Mins"]>300) | (data["State"]=="NY")]
print(data4)

# Minuts on day, on night and account's longitude of the first 50
subset_first_50 = data[["Day Mins", "Night Mins", "Account Length"]][:50]

print(subset_first_50.head)

# Columns and rows
print(data.ix[1:10, 3:6]) # First 10 rows, columns from 3 to 6

# Previous one, ix, is deprecated, so the new one is:
print(data.iloc[1:10, 3:6])

print(data.iloc[1:10], [2, 5, 7])

# By name, we use loc
print(data.loc[[1, 3], ["Area Code", "VMail Plan"]])

# Add a new column
data["Total Mins"] = data["Day Mins"] + data["Night Mins"] + data["Eve Mins"]

print(data["Total Mins"].head)