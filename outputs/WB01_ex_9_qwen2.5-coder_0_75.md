Thoughts:
The task requires writing Python code without using functions. We will use variables directly to solve the problem of converting an amount from Euros (EUR) to Pounds Sterling (GBP), taking into account a 2% commission by the exchange house.

Python Code:

```python
# Define the amount in Euros and the exchange rate
amount_eur = 1000
exchange_rate = 0.90

# Calculate the total amount after adding the commission
total_amount_with_commission = amount_eur * (1 + 2 / 100)

# Convert the total amount to Pounds Sterling
amount_gbp = total_amount_with_commission * exchange_rate

# Print the equivalent amount in pounds
print("The equivalent amount in GBP is:", amount_gbp, "GBP")
```

This code directly defines the variables for `amount_eur` and `exchange_rate`. It calculates the total amount after adding a 2% commission by multiplying the Euro amount by `(1 + 2 / 100)`. Then, it converts this total amount to Pounds Sterling using the provided exchange rate. Finally, it prints out the equivalent amount in GBP.

This solution adheres to the requirements of not using functions and directly uses variables for input data, providing a straightforward implementation of the given problem.