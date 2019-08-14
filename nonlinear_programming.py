import numpy as np
from scipy.optimize import minimize

# Our objective function
def rosen(x):
	return sum(100 * (x[1:] - x[:-1] ** 2) ** 2 + (1 - x[:-1]) ** 2)

# Initial guesses (random) for x0 and x1
x = np.array([1.3, 0.7])

# Optimizes the problem using the Nelder-Mead method
# with termination tolerance on x
result = minimize(rosen, x, method = 'nelder-mead', \
	options = {'xtol': 1e-8, 'disp': True})

# Prints the value of x and objective evaluated in that value
print(result.x)
print(rosen(result.x))