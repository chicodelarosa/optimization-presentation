from platypus import Problem, Real, SPEA2, NSGAII

# Our objective functions
def schaffer(x):
    return [ x[0] ** 2, (x[0] - 2) ** 2 ]

# Instatiates a Problem object with 1 variable and 2 objective functions
problem = Problem(1, 2)

# Sets variable as real with bounds between -10 and 10
problem.types[:] = Real(-10, 10)

# Sets the problem function instance to our objective function
problem.function = schaffer

# Uses the Non-dominated Selection Genetic Algorithm 2 with 50 particles
# to optimize our problem
algorithm = NSGAII(problem, population_size = 50)
# algorithm = SPEA2(problem, population_size = 50)

# Optimizes the problem in 10000 iterations
algorithm.run(10000)

# Gets the solutions of each particle
solutions = algorithm.population

# Prints the value of x and objectives evaluated in that value
print("Value of x = %.2f " % solutions[0].variables[0])
print("Value of f1 = %.2f and f2 = %.2f" % \
	(solutions[0].objectives[0], solutions[0].objectives[1]))