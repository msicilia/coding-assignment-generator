### Problem Description:
Write Python code to perform a cost calculation for a truck on a trip. The inputs include distance traveled in kilometers, liters of diesel used, cost per liter of diesel, and other maintenance costs. The output should include kilometers travelled per litre, total cost of the trip, and total cost per kilometer.

### Constraints:
- No functions are allowed.
- Only variables can be used for input values.

### Example Test Cases:
1. Distance: 300 km, Diesel Used: 10 liters, Cost Per Liter: 2.8, Other Costs: 50
   - Expected Output: Kilometres Travelled per Litre = 30.0, Total Cost of the Trip = 78.0, Total Cost per Kilometer = 0.26

2. Distance: 750 km, Diesel Used: 25 liters, Cost Per Liter: 3.0, Other Costs: 120
   - Expected Output: Kilometres Travelled per Litre = 30.0, Total Cost of the Trip = 185.0, Total Cost per Kilometer = 0.2467

3. Distance: 100 km, Diesel Used: 5 liters, Cost Per Liter: 2.2, Other Costs: 30
   - Expected Output: Kilometres Travelled per Litre = 20.0, Total Cost of the Trip = 60.0, Total Cost per Kilometer = 0.6

### Python Code:

```py
# Define the variables for the inputs
distance_km = 300  # Distance travelled in kilometers
diesel_liters = 10  # Litres of diesel used
cost_per_liter = 2.8  # Cost per litre of diesel
other_costs = 50  # Other maintenance costs

# Calculate the kilometres travelled per litre
km_per_liter = distance_km / diesel_liters

# Calculate the total cost of the trip
total_cost_trip = (diesel_liters * cost_per_liter) + other_costs

# Calculate the total cost per kilometre
cost_per_km = total_cost_trip / distance_km

# Print the results
print("Kilometres Travelled per Litre:", km_per_liter)
print("Total Cost of the Trip:", total_cost_trip)
print("Total Cost per Kilometer:", cost_per_km)
```

### Explanation:
1. **Input Variables**: The inputs are defined as variables `distance_km`, `diesel_liters`, `cost_per_liter`, and `other_costs`.
2. **Calculations**:
   - **Kilometres Travelled per Litre**: This is calculated by dividing the distance travelled by the litres of diesel used.
   - **Total Cost of the Trip**: This includes both the cost of diesel and other maintenance costs.
   - **Total Cost per Kilometer**: This is obtained by dividing the total cost of the trip by the distance travelled.
3. **Output**: The results are printed to provide the desired outputs.

This code adheres to the constraints given in the problem statement, using only variables without any functions or input calls.