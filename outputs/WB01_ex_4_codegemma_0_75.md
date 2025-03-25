```python
# Define variables for the trip
distance_travelled = 500
litres_of_diesel_used = 150
cost_per_litre_of_diesel = 1.20
maintenance_costs = 200

# Calculate the kilometres travelled per litre
kilometers_per_litre = distance_travelled / litres_of_diesel_used

# Calculate the total cost of the trip
total_cost_of_trip = (litres_of_diesel_used * cost_per_litre_of_diesel) + maintenance_costs

# Calculate the total cost per kilometre
total_cost_per_kilometre = total_cost_of_trip / distance_travelled

# Print the results
print("Kilometers travelled per litre:", kilometers_per_litre)
print("Total cost of the trip:", total_cost_of_trip)
print("Total cost per kilometre:", total_cost_per_kilometre)
```