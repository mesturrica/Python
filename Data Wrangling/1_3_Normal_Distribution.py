import numpy as np
import matplotlib.pyplot as plt

# Normal distribution

data = np.random.randn(100)
x = range(1,101)

# We generate the plot, to see the data
plt.plot(x, data)

# Util to see the data we generated.
print(data)


# Mean
mu = 5.5
standard_deviation = 2.5

data = mu + standard_deviation * np.random.randn(10000)

print(data)