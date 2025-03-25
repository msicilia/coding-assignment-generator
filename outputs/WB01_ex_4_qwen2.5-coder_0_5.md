```python
# User input variables
distance_km = 200
litres_diesel = 40
cost_per_litre_diesel = 1.3
other_costs = 80

# Calculating kilometres travelled per litre
km_per_litre = distance_km / litres_diesel

# Calculating total cost of the trip
total_cost_trip = (litres_diesel * cost_per_litre_diesel) + other_costs

# Calculating total cost per kilometre
cost_per_km = total_cost_trip / distance_km

# Outputting the results
print("Kilometres travelled per litre:", km_per_litre)
print("Total cost of the trip:", total_cost_trip)
print("Total cost per kilometre:", cost_per_km)
```

This Python code performs the cost calculation for a truck on a trip by using variables to store the input data, such as distance travelled in kilometres, litres of diesel used, cost per litre of diesel, and other costs. It then calculates the kilometres travelled per litre, total cost of the trip, and total cost per kilometre using arithmetic operations. Finally, it outputs the results to the console.

You can modify the values of `distance_km`, `litres_diesel`, `cost_per_litre_diesel`, and `other_costs` variables to test different scenarios and see how the code calculates the costs for each trip.