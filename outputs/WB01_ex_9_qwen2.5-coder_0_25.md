Thought: The task requires calculating the equivalent amount in Pounds Sterling (GBP) for a given amount in Euros (EUR), considering a 2% commission from the exchange house. We cannot use functions, so we need to write the logic using only basic statements and control structures.

Let's break down the steps:

1. **Input the amount in EUR and the exchange rate**: Since we cannot use `input()`, we will assume these values are provided as variables.
2. **Calculate the total amount before commission** by multiplying the amount in EUR by the exchange rate.
3. **Calculate the commission** by finding 2% of the total amount before commission.
4. **Subtract the commission from the total amount** to get the final amount in GBP.
5. **Print the result**.

Here is the Python code to achieve this:

```python
# Define the variables for the amount in EUR and the exchange rate
eur_amount = 100  # Example amount in EUR
exchange_rate = 0.85  # Example exchange rate (EUR per GBP)

# Calculate the total amount before commission
total_before_commission = eur_amount * exchange_rate

# Calculate the commission (2% of the total amount)
commission = total_before_commission * 0.02

# Calculate the final amount in GBP after subtracting the commission
gbp_amount = total_before_commission - commission

# Print the result
print("The equivalent amount in GBP is:", gbp_amount)
```

### Example Test Cases:

1. **Test Case 1**:
   ```python
   eur_amount = 100
   exchange_rate = 0.85
   ```
   **Expected Output**:
   ```
   The equivalent amount in GBP is: 83.7
   ```

2. **Test Case 2**:
   ```python
   eur_amount = 500
   exchange_rate = 0.90
   ```
   **Expected Output**:
   ```
   The equivalent amount in GBP is: 441.0
   ```

3. **Test Case 3**:
   ```python
   eur_amount = 200
   exchange_rate = 0.80
   ```
   **Expected Output**:
   ```
   The equivalent amount in GBP is: 156.8
   ```

This code and the provided test cases should help you understand how to calculate the equivalent amount in GBP while considering a 2% commission from the exchange house, without using any functions.