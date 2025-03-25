To solve the problem of calculating change for a supermercado, we need to create a function that takes two arguments: the amount paid by the customer and the purchase amount. The function will then calculate the difference (change) and output how many pieces of each denomination should be given as change. We must use loops and basic iteration without using data structures like lists or dictionaries.

Here's the Python code to achieve this:

```python
def calculate_change(paid_amount, purchase_amount):
    denominations = [500.0, 200.0, 100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    change = paid_amount - purchase_amount
    
    print("Change:")
    
    for denom in denominations:
        if change >= denom:
            count = int(change // denom)
            change -= count * denom
            print(f"{count} piece(s) of {denom} euro{'s' if count > 1 else ''}")

# Example test cases
calculate_change(50.75, 32.49)
calculate_change(100.00, 85.60)
```

Explanation:
1. **Denominations List**: We define a list of possible denominations.
2. **Change Calculation**: The change is calculated as the difference between the paid amount and the purchase amount.
3. **Loop Through Denominations**: We loop through each denomination from the largest to the smallest.
4. **Count Pieces**: For each denomination, we determine how many pieces are needed by integer division (`count = int(change // denom)`).
5. **Update Change**: We subtract the value of the given pieces from the total change.
6. **Output**: We print out the number of pieces for each denomination if it's greater than zero.

This function ensures that only non-zero denominations are outputted, meeting the requirement to avoid specifying denominations for which no change is needed.