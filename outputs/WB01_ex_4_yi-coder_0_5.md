Here's a Python code that performs the cost calculation for a truck on a trip:

```python
def calculateCost(distance, dieselLitres, dieselPrice, maintainance):
    kmPerLiter = distance / dieselLitres
    totalCost = (dieselLitres * dieselPrice) + maintainance
    costPerKm = totalCost / distance

    return kmPerLiter, totalCost, costPerKm
```

You can test the function with the following example:

```python
kmPerLiter, totalCost, costPerKm = calculateCost(100, 25, 1.5, 50)
print('KM Per Liter: ' + str(kmPerLiter))
print('Total Cost: ' + str(totalCost))
print('Cost Per KM: ' + str(costPerKm))
```