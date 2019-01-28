import pandas as pd
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Plots and data Visualization

main_path = "Datasets/"
filepath = "customer-churn-model/Customer Churn Model.txt"

data = pd.read_csv(os.path.join(main_path, filepath))

print(data)

# We get the number of columns to apply Sturges Algorithm
data_number = data.shape[0]

print(data_number)

# Print Sturges Algorithm
sturges = 1 + np.log2(data_number)
sturges = int(np.ceil(sturges))
print(sturges)

# We print an histogram of calls
histogram = plt.hist(data["Day Calls"], bins=sturges)
plt.xlabel = ("Number of calls in the Day")
plt.ylabel = ("Frequency")
