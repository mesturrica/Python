# First, we generate the seed
import numpy as np

seed = np.random.seed(2018)

# We get same results, inside the random ones.
for i in range(5):
    print(np.random.random())