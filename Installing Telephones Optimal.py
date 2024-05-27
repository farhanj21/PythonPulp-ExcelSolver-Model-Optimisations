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
