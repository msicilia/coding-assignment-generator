 Code:
   ```python
   distance_travelled = 500  # kilometers
   diesel_used = 80         # litres
   cost_per_litre = 1.2      # dollars/litre
   maintenance_costs = 300   # dollars (grouped value)

   # Calculate kilometres travelled per litre (fuel efficiency)
   fuel_efficiency = distance_travelled / diesel_used

   # Calculate total cost of the trip (diesel + maintenance)
   total_cost_trip = (diesel_used * cost_per_litre) + maintenance_costs

   # Calculate total cost per kilometre (including both fuel and maintenance costs)
   total_cost_per_km = total_cost_trip / distance_travelled

   print(f"Fuel Efficiency: {fuel_efficiency} km/l")
   print(f"Total Cost of the Trip: ${total_cost_trip}")
   print(f"Total Cost per Kilometre: ${total_cost_per_km}")
   ```

   Explanation: The code assigns values to variables representing the data given for a truck on a trip. It then calculates the fuel efficiency, total cost of the trip, and total cost per kilometre using mathematical operations. Finally, it prints these calculated values in a readable format.