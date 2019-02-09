import pandas as pd

# First, we read a local csv
data = pd.read_csv('../Datasets/customer-churn-model/Customer Churn Model.txt')

# We print data to see that we're loading correctly.
print(data.head())

# Creation of a data subset
account_length = data["Account Length"]

print(account_length.head())

# To see the type of the object
print(type(account_length))

# More than one column subset
subset = data[["Account Length", "Phone", "Eve Charge"]]
print(subset.head())

print(type(subset))

desired_columns = ["Account Length", "Phone", "Eve Charge", "Night Calls"]
subset = data[desired_columns]

print(subset.head())

# To get all columns
all_columns = data.columns.values.tolist()
print(all_columns)

# Complementary list
sublist = (x for x in all_columns if x not in desired_columns )


# Another way to do a complementary list
a = set(desired_columns)
b = set(all_columns)
sublist = b-a
sublist = list(sublist)
