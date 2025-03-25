  Write a code that performs the cost calculation for a truck on a trip, knowing that on each trip, the driver records the distance travelled in kilometres, the litres of diesel used, the cost per litre of diesel and other costs (as a single grouped value) of maintaining the truck. As part of the accounting process, the controller needs to calculate, for the truck and the trip, the kilometres travelled per litre, the total cost of the trip and the total cost per kilometre (including maintenance costs).

```
distance = 100
liters_used = 50
cost_per_liter = 2.50
other_costs = 30.00
total_cost = round(cost_per_liter * liters_used + other_costs, 2)
print("Total cost of the trip: ", total_cost)
kms_per_liter = distance / liters_used
print("Kilometres per liter: ", kms_per_liter)
```
In this code, we first define some variables to represent the data for the truck and the trip. We then calculate the total cost of the trip by multiplying the cost per liter of diesel by the number of liters used and adding any other costs (e.g., maintenance costs). Finally, we print out the total cost and the number of kilometres per litre using the `print()` function.