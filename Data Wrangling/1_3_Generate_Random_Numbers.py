import pandas as pd
import numpy as np
import random


# First, we read a local csv
data = pd.read_csv('../Datasets/customer-churn-model/Customer Churn Model.txt')

# Generating a random number
print(np.random.randint(1, 1000000))

# Random between 0 and 1
print(np.random.random())


# Function that generates a list of n random integer numbers in a interval [a,b]
def randint_list(n, a, b):
    x = []
    for i in range(n):
        x.append(np.random.randint(a,b))
    return x

print(randint_list(10, 1, 50 ))

# Same as before but with util
for i in range(10):
    print(random.randrange(0, 100, 7))

# Shuffling, in other words, merge.

a = np.arange(100)
print(a)

# We shuffle a
print(np.random.shuffle(a))

print(a)

# Choice Method, it generates a random one inside a set.
column_values = data.columns.values.tolist()
print(column_values)

print(np.random.choice(column_values))