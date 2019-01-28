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