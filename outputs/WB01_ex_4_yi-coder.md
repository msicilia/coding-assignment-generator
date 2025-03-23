Here is a Python code snippet that calculates the required values:
```py
# initialize variables for a single trip
km = 200  # distance travelled in kilometers
litres = 50  # litres of diesel used
diesel_cost = 1.3  # cost per litre of diesel
maintenance_cost = 40  # other costs (as a single grouped value) of maintaining the truck

# calculate kilometres travelled per litre
km_per_litre = km / litres

# calculate total cost of the trip
total_trip_cost = (litres * diesel_cost) + maintenance_cost

# calculate total cost per kilometre
cost_per_km = total_trip_cost / km

print("Kilometers travelled per litre: ", km_per_litre)
print("Total cost of the trip: ", total_trip_cost)
print("Cost per kilometer (including maintenance costs): ", cost_per_km)
```

In this example, the values are directly embedded in the code. To use different values for a different trip, simply change the value assigned to `km`, `litres`, `diesel_cost` and `maintenance_cost` as needed.