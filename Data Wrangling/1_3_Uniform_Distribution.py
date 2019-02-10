import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# We generate random uniform distributed data ( all values has the same probability to appear)
a = 1
b = 100
n = 1000

data = np.random.uniform(a, b, n)

# We see the generated values.
print(data)

# We generate the plot to see if the data is uniform.
plot = plt.hist(data)



