import numpy as np

# We generate 2 random numbers between 0 and 1
# Calculate x * x + y * y
# If the value is below 1 we're inside the circle, if the value is more than 1 , we're out of the circle
# We calculate the total number of moments we're inside the circle and we divide it by the total number of tries to have an
# aproximation of the probability of being inside the circle

# We repeat the experiment a certain number of times(for example 1000) to obtain different approximations of PI

pi_avg = 0
pi_value_list = []
n = 1000
for i in range(100):
    value = 0
    x = np.random.uniform(0, 1, n).tolist()
    y = np.random.uniform(0, 1, n).tolist()
    for j in range(n):
        z = np.sqrt(x[j] * x[j] + y[j] * y[j])
        # We're inside the circle
        if z <= 1:
            value +=1
    float_value = float(value)
    pi_value = float_value * 4 / n
    pi_value_list.append(pi_value)
    pi_avg += pi_value

pi = pi_avg / 100

print(pi)