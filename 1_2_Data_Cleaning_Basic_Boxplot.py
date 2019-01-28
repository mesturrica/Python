import pandas as pd
import os
import matplotlib
import matplotlib.pyplot as plt

# Plots and data Visualization

main_path = "Datasets/"
filepath = "customer-churn-model/Customer Churn Model.txt"

data = pd.read_csv(os.path.join(main_path, filepath))

print(data)

# We print the boxplot with a label on the y axis.
plt.boxplot(data["Day Calls"])
plt.ylabel("Number of calls on a Day")
plt.title("Boxplot of calls on a Day")


# Inter Quartile Range
IQR = data["Day Calls"].quantile(0.75) - data["Day Calls"].quantile(0.25)
print(IQR)

minBox = data["Day Calls"].quantile(0.25) - 1.5 * IQR
print(minBox)

maxBox = data["Day Calls"].quantile(0.75) + 1.5 * IQR
print(maxBox)

# Values that are below or upper of the box, are outlayers