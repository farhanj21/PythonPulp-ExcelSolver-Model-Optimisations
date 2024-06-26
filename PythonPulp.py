# -*- coding: utf-8 -*-
"""OR Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sPzp4o-O1Bz2SIIrmVmbo-d84pqFuSnz
"""

#Example 2.4-4 (Multiperiod Production Smoothing Model)
#!pip install pulp
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

#Example 2.4-5 (Bus Scheduling Model)
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpStatus

#linear programming problem
model = LpProblem(name="Bus_Scheduling", sense=LpMinimize)

#decision variables
x1 = LpVariable(name="x1", lowBound=0, cat="Integer")
x2 = LpVariable(name="x2", lowBound=0, cat="Integer")
x3 = LpVariable(name="x3", lowBound=0, cat="Integer")
x4 = LpVariable(name="x4", lowBound=0, cat="Integer")
x5 = LpVariable(name="x5", lowBound=0, cat="Integer")
x6 = LpVariable(name="x6", lowBound=0, cat="Integer")

#Objective function
model += lpSum([x1, x2, x3, x4, x5, x6]), "Total_Buses"

#Constraints
model += x1 + x6 >= 4, "12:01 a.m.–4:00 a.m."
model += x1 + x2 >= 8, "4:01 a.m.–8:00 a.m."
model += x2 + x3 >= 10, "8:01 a.m.–12:00 noon"
model += x3 + x4 >= 7, "12:01 p.m.–4:00 p.m."
model += x4 + x5 >= 12, "4:01 p.m.–8:00 p.m."
model += x5 + x6 >= 4, "8:01 p.m.–12:00 p.m."

#Solve the problem
model.solve()

#Display
print(f"Status: {LpStatus[model.status]}")
print(f"Total Buses: {model.objective.value()}")
print("Optimal Schedule:")
print(f"x1 = {x1.value()}, buses starting at 12:01 a.m.")
print(f"x2 = {x2.value()}, buses starting at 4:01 a.m.")
print(f"x3 = {x3.value()}, buses starting at 8:01 a.m.")
print(f"x4 = {x4.value()}, buses starting at 12:01 p.m.")
print(f"x5 = {x5.value()}, buses starting at 4:01 p.m.")
print(f"x6 = {x6.value()}, buses starting at 8:01 p.m.")

#Example 5.3-1 (SunRay Transport)
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, value

#Supply and demand
supply = [15, 25, 10]  # Supply at each source (Silo)
demand = [5, 15, 15, 15]  # Demand at each destination (Mill)

# Transportation costs
costs = [
    [10, 2, 20, 11],
    [12, 7, 9, 20],
    [4, 14, 16, 18]
]

#Linear programming problem
model = LpProblem(name="SunRayTransportation", sense=LpMinimize)

#Decision variables
num_sources = len(supply)
num_destinations = len(demand)
x = [[LpVariable(f"x{i + 1}{j + 1}", lowBound=0) for j in range(num_destinations)] for i in range(num_sources)]

#Objective function
model += lpSum(x[i][j] * costs[i][j] for i in range(num_sources) for j in range(num_destinations))

#Constraints for supply
for i in range(num_sources):
    model += lpSum(x[i][j] for j in range(num_destinations)) == supply[i]

#Constraints for demand
for j in range(num_destinations):
    model += lpSum(x[i][j] for i in range(num_sources)) == demand[j]

#Solve problem using Northwest-corner method
for i in range(num_sources):
    for j in range(num_destinations):
        quantity = min(supply[i], demand[j])
        model += x[i][j] == quantity
        supply[i] -= quantity
        demand[j] -= quantity

#Solve the linear programming problem
model.solve()

#Display
print("Status:", pulp.LpStatus[model.status])
print("Objective Value (Total Cost):", value(model.objective))

#Display the optimal transportation schedule
for i in range(num_sources):
    for j in range(num_destinations):
        if value(x[i][j]) != 0:
            print(f"Ship {x[i][j].name} = {value(x[i][j])}")

#Example 9.1-2 (Installing Security Telephones)
import pulp

# Create a minimization problem
model = pulp.LpProblem("Minimize_Telephones_Installation", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("Telephone_Installed", range(1, 9), 0, 1, pulp.LpBinary)

# Objective function
model += pulp.lpSum(x[j] for j in range(1, 9)), "Total_Telephones_Installed"

# Constraints
model += x[1] + x[2] >= 1, "Street_A"
model += x[2] + x[3] >= 1, "Street_B"
model += x[4] + x[5] >= 1, "Street_C"
model += x[7] + x[8] >= 1, "Street_D"
model += x[6] + x[7] >= 1, "Street_E"
model += x[2] + x[6] >= 1, "Street_F"
model += x[1] + x[6] >= 1, "Street_G"
model += x[4] + x[7] >= 1, "Street_H"
model += x[2] + x[4] >= 1, "Street_I"
model += x[5] + x[8] >= 1, "Street_J"
model += x[3] + x[5] >= 1, "Street_K"

# Solve the problem
model.solve()

# Print the results
print("Status:", pulp.LpStatus[model.status])
print("Optimal Solution:")
for j in range(1, 9):
    installation_status = "1.0 (Telephone Installed)" if pulp.value(x[j]) == 1.0 else f"{pulp.value(x[j]):.1f}"
    print(f"Intersection {j}: {installation_status}")

print("Total Telephones Installed:", pulp.value(model.objective))

#Example 9.1-3 (Choosing a Telephone company)
from pulp import LpProblem, LpMinimize, LpVariable, lpSum

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
print("Status:", pulp.LpStatus[model.status])
print("Optimal Solution:")
print("x1 =", value(x1))
print("x2 =", value(x2))
print("x3 =", value(x3))
print("y1 =", value(y1))
print("y2 =", value(y2))
print("y3 =", value(y3))
print("Total Cost =", value(prob.objective))