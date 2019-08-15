from pulp import *

# Creates the 'problem' object to contain the problem data
problem = LpProblem("The Car Additive Optimization Problem", LpMaximize)

# Creates the variables
a1 = LpVariable("Additive 1", 0, None, LpContinuous)
a2 = LpVariable("Additive 2", 0, None, LpContinuous)

# Sets the objective function
# f = 7.5 * a1 + 5.2 * a2
f = 1.2 * a1 + 2.1 * a2

# Adds the objective function to the problem object
problem += f, "Speed to maximize"

# Adds the constraints to the problem object
problem += 3.1 * a1 + 4.8 * a2 <= 15, "Compound A constraint"
problem += 2.4 * a1 + a2 <= 5, "Compound B constraint"

# The problem is optimized
problem.solve()

# The status gets printed to the screen
print("Status:", LpStatus[problem.status])

# The variables get printed with their resolved value
for v in problem.variables():
    print(v.name, "=", "%.2f" % v.varValue)

# The optimized objective function value gets printed to the screen
print("Speed can be maximized by %.2f" % value(problem.objective), "units!")