 Code:
```python
# Input values
distance_travelled = 500  # kilometers
litres_diesel_used = 80  # liters
cost_per_liter_diesel = 1.20  # dollars per liter
maintenance_costs = 300  # dollars for the trip

# Calculations
kilometers_per_liter = distance_travelled / litres_diesel_used
total_cost_trip = (litres_diesel_used * cost_per_liter_diesel) + maintenance_costs
total_cost_per_kilometer = total_cost_trip / distance_travelled

# Output results
print("Kilometers per liter:", kilometers_per_liter)
print("Total cost of the trip:", total_cost_trip)
print("Total cost per kilometer:", total_cost_per_kilometer)
```