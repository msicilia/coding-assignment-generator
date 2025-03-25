 To solve this problem, I will write a Python function that takes the total amount of a purchase and the amount paid by the customer as input. The function will calculate the change due to the customer and then determine the number of each type of bill or coin that needs to be given as change. The function will print out the result in a readable format, specifying only the pieces for which there are one or more units to be given.

Here is the Python code:

```python
def calculate_change(total, paid):
    # List of available bill and coin denominations in Euros
    denominations = [500.0, 200.0, 100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

    change = paid - total

    # Loop through each denomination to calculate the number of pieces needed for change
    for denomination in denominations:
        num_pieces = int(change / denomination)
        if num_pieces > 0:
            print(f"{num_pieces} piece(s) of {denomination} Euro")
            change -= num_pieces * denomination

# Test cases
calculate_change(153.27, 200)
calculate_change(56.89, 100)
```

This code defines a function `calculate_change` that takes two arguments: the total amount of the purchase and the amount paid by the customer. It then calculates the change due to the customer and iterates through each denomination of bill or coin available in Euros. For each denomination, it calculates the number of pieces needed for change using integer division and checks if that number is greater than zero. If so, it prints out the result and subtracts the value of those pieces from the total change due. The function continues to do this until all denominations have been considered.

The test cases at the end demonstrate how to use the function to calculate the change for two different purchases.