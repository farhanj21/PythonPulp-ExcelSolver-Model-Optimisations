#Example 2.4-4 (Multiperiod Production Smoothing Model)
#pip install pulp
from pulp import LpProblem, LpMinimize, LpVariable, lpSum

#linear programming problem
model = LpProblem(name="Multiperiod Production Smoothing Model", sense=LpMinimize)

#decision variables
x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)
x3 = LpVariable("x3", lowBound=0)
x4 = LpVariable("x4", lowBound=0)

S1_minus = LpVariable("S1_minus", lowBound=0)
S2_minus = LpVariable("S2_minus", lowBound=0)
S3_minus = LpVariable("S3_minus", lowBound=0)
S4_minus = LpVariable("S4_minus", lowBound=0)

S1_plus = LpVariable("S1_plus", lowBound=0)
S2_plus = LpVariable("S2_plus", lowBound=0)
S3_plus = LpVariable("S3_plus", lowBound=0)
S4_plus = LpVariable("S4_plus", lowBound=0)

I1 = LpVariable("I1", lowBound=0)
I2 = LpVariable("I2", lowBound=0)
I3 = LpVariable("I3", lowBound=0)

#objective function
model += 50 * (I1 + I2 + I3) + 200 * (S1_minus + S2_minus + S3_minus + S4_minus) + 400 * (S1_plus + S2_plus + S3_plus + S4_plus)

#constraints
model += 10 * x1 == 400 + I1
model += I1 + 10 * x2 == 600 + I2
model += I2 + 10 * x3 == 400 + I3
model += I3 + 10 * x4 == 500

model += x1 == S1_minus - S1_plus
model += x2 == x1 + S2_minus - S2_plus
model += x3 == x2 + S3_minus - S3_plus
model += x4 == x3 + S4_minus - S4_plus

# Solve the optimization problem
model.solve()

# Display
print(f"Optimal Solution:")
print(f"Objective Value (Z): ${model.objective.value():,.2f}")

for var in model.variables():
    print(f"{var.name}: {var.value()}")

