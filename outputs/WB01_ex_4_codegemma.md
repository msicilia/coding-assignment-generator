```python
# Define variables
distance = 1200
diesel_used = 60
diesel_cost = 2.50
maintenance_cost = 300

# Calculate kilometres travelled per litre
kpl = distance / diesel_used

# Calculate total cost of the trip
total_cost = diesel_used * diesel_cost + maintenance_cost

# Calculate total cost per kilometre
total_cost_per_kilometer = total_cost / distance

# Print the results
print("Kilometres travelled per litre:", kpl)
print("Total cost of the trip:", total_cost)
print("Total cost per kilometre:", total_cost_per_kilometer)
```

**Output:**

```
Kilometres travelled per litre: 20.0
Total cost of the trip: 450.0
Total cost per kilometre: 0.375
```