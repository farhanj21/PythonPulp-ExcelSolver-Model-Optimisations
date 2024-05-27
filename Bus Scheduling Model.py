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
