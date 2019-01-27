import pandas as pd
import os
import matplotlib
import matplotlib.pyplot as plt

# Plots and data Visualization

main_path = "Datasets/"
filepath = "customer-churn-model/Customer Churn Model.txt"

data = pd.read_csv(os.path.join(main_path, filepath))

print(data)

# % matplotlib inline

# to save the plot:  savefig("path of the file.jpeg")

# Scatter Plot
print(data.plot(kind="scatter", x="Day Mins", y="Day Charge"))
data32 = data.plot(kind="scatter", x="Day Mins", y="Day Charge").get_figure()
data32.savefig("scatterplot.png")

figure, axs = plt.subplots(2,2, sharey="all", sharex="all")

data.plot(kind="scatter", x="Day Mins", y="Day Charge", ax= axs[0][0])
data.plot(kind="scatter", x="Night Mins", y="Night Charge", ax = axs[0][1])
data.plot(kind="scatter", x="Day Calls", y="Day Charge", ax= axs[1][0])
data.plot(kind="scatter", x="Night Calls", y="Night Charge", ax = axs[1][1])


