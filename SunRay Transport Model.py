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
