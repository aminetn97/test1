from turtle import mode
from pyomo.environ import *

# Create a model
model = ConcreteModel()

# Define decision variables
model.x = Var(domain=NonNegativeReals)  # Quantity of product 1
model.y = Var(domain=NonNegativeReals)  # Quantity of product 2

# Define the objective function (maximize profit)
model.obj = Objective(expr=40 * model.x + 30 * model.y, sense=maximize)

# Define constraints (resource limitations)
model.constraints = ConstraintList()
model.constraints.add(10 * model.x + 3 * model.y >= model.y)  # Labor hours constraint
model.constraints.add(model.x*(0.2) + 4 >=model.y)  # Limit on product 1
model.constraints.add(model.x* (-0.2) + 6 >= model.y)  # Limit on product 2

# Create a solver
solver = SolverFactory('glpk')

# Solve the model
results = solver.solve(model)

# Display the results
model.display()

# Print the optimal solution
print("\nOptimal Solution:")
print(f"Product 1 (x): {model.x()} units")
print(f"Product 2 (y): {model.y()} units")
print(f"Total Profit: ${model.obj()}")

# Display the solver results
results.write()
