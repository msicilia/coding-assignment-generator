Sure, let's write the Python code that performs the required calculations without using functions. We'll use variables instead to exercise the code.

Here is the complete solution:

```py
# Define the variables for each test case
distance_test1 = 300  # Distance travelled in kilometres
litres_used_test1 = 50  # Litres of diesel used
cost_per_litre_test1 = 7.5  # Cost per litre of diesel
maintenance_costs_test1 = 200  # Maintenance costs

distance_test2 = 450  # Distance travelled in kilometres
litres_used_test2 = 60  # Litres of diesel used
cost_per_litre_test2 = 8.0  # Cost per litre of diesel
maintenance_costs_test2 = 300  # Maintenance costs

distance_test3 = 600  # Distance travelled in kilometres
litres_used_test3 = 75  # Litres of diesel used
cost_per_litre_test3 = 8.5  # Cost per litre of diesel
maintenance_costs_test3 = 400  # Maintenance costs

# Calculate for Test Case 1
km_per_litre_test1 = distance_test1 / litres_used_test1
total_cost_test1 = (litres_used_test1 * cost_per_litre_test1) + maintenance_costs_test1
cost_per_km_test1 = total_cost_test1 / distance_test1

# Print the results for Test Case 1
print("Test Case 1:")
print(f"Kilometres travelled per litre: {km_per_litre_test1:.2f}")
print(f"Total cost of the trip: {total_cost_test1:.2f}")
print(f"Total cost per kilometre: {cost_per_km_test1:.2f}")

# Calculate for Test Case 2
km_per_litre_test2 = distance_test2 / litres_used_test2
total_cost_test2 = (litres_used_test2 * cost_per_litre_test2) + maintenance_costs_test2
cost_per_km_test2 = total_cost_test2 / distance_test2

# Print the results for Test Case 2
print("\nTest Case 2:")
print(f"Kilometres travelled per litre: {km_per_litre_test2:.2f}")
print(f"Total cost of the trip: {total_cost_test2:.2f}")
print(f"Total cost per kilometre: {cost_per_km_test2:.2f}")

# Calculate for Test Case 3
km_per_litre_test3 = distance_test3 / litres_used_test3
total_cost_test3 = (litres_used_test3 * cost_per_litre_test3) + maintenance_costs_test3
cost_per_km_test3 = total_cost_test3 / distance_test3

# Print the results for Test Case 3
print("\nTest Case 3:")
print(f"Kilometres travelled per litre: {km_per_litre_test3:.2f}")
print(f"Total cost of the trip: {total_cost_test3:.2f}")
print(f"Total cost per kilometre: {cost_per_km_test3:.2f}")
```

### Explanation:
1. **Variables for Test Cases**: We define variables for each test case with distances, litres of diesel used, cost per litre, and maintenance costs.
2. **Calculations**:
   - `km_per_litre` is calculated by dividing the distance by the litres of diesel used.
   - `total_cost` is calculated by multiplying the litres of diesel used by the cost per litre and adding the maintenance costs.
   - `cost_per_km` is calculated by dividing the total cost by the distance.
3. **Print Statements**: The results for each test case are printed with formatted output to display two decimal places.

This code performs the required calculations without using functions, as requested in the problem statement.