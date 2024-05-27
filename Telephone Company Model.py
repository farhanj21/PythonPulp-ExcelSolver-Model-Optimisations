from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpStatus, value

# Create a linear programming problem
prob = LpProblem("TelephoneCompany", LpMinimize)

# Define decision variables
x1 = LpVariable("x1", lowBound=0, cat="Continuous")
x2 = LpVariable("x2", lowBound=0, cat="Continuous")
x3 = LpVariable("x3", lowBound=0, cat="Continuous")

y1 = LpVariable("y1", cat="Binary")
y2 = LpVariable("y2", cat="Binary")
y3 = LpVariable("y3", cat="Binary")

# Define the objective function
prob += 0.25 * x1 + 0.21 * x2 + 0.22 * x3 + 16 * y1 + 25 * y2 + 18 * y3, "TotalCost"

# Define the constraints
prob += x1 + x2 + x3 == 200, "TotalMinutes"
prob += x1 <= 200 * y1, "MaBellConstraint"
prob += x2 <= 200 * y2, "PaBellConstraint"
prob += x3 <= 200 * y3, "BabyBellConstraint"

# Solve the problem
prob.solve()

# Display the results
print("Status:", LpStatus[prob.status])
print("Optimal Solution:")
print("x1 =", value(x1))
print("x2 =", value(x2))
print("x3 =", value(x3))
print("y1 =", value(y1))
print("y2 =", value(y2))
print("y3 =", value(y3))
print("Total Cost =", value(prob.objective))
