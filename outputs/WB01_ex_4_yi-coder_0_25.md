Here is a Python code that meets all given requirements:

```python
# Variables as example test case
kilometres = 500  # distance travelled in kilometers
litres = 40      # litres of diesel used
cost_per_litre = 1.2   # cost per litre of diesel
maintenance_cost = 300    # other costs (maintenance)
```

Then, the calculations required by the task:

```python
# Calculations for the truck and trip
km_per_litre = kilometres / litres  # km travelled per litre
total_trip_cost = (litres * cost_per_litre) + maintenance_cost   # total cost of the trip
cost_per_km = total_trip_cost / kilometres    # total cost per km (including maintenance costs)
```

In this code, we first calculate the number of kilometers travelled per litre using division. Then, we calculate the total cost of the trip by multiplying the cost per litre with the number of litres used and adding the maintenance cost. Finally, to get the cost per km, we divide the total trip cost by the distance travelled in kilometers.

We have not used functions as requested because it seems that no separate function needs to be defined to perform these calculations. 

This code does not use input() calls for reading data from the keyboard and uses variables for test cases instead.