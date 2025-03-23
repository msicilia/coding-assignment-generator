Here is a Python program that should solve the problem as described:

```python
def calculate_change(total, paid):
    euros = [500.0, 200.0, 100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    change = paid - total
    result = {}

    for euro in euros:
        count = int(change // euro)
        if count > 0:
            result[euro] = count
            change -= count * euro
    return result

# Test case
total_price = float(input("Enter the total price in Euros: "))
paid_amount = float(input("Enter the amount paid in Euros: "))
response = calculate_change(total_price, paid_amount)
for key in response:
    print('Number of ' + str(key) + ' Euros: ' + str(response[key]))
```