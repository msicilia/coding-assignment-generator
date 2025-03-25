Certainly! Below is a Python code snippet that meets all the specified requirements:

```python
# Define variables for testing purposes
purchase_amount = "120"  # Replace this with actual input in your environment
payment_method = "cash"   # Replace this with actual input in your environment

try:
    # Convert purchase amount to float
    purchase_amount = float(purchase_amount)
    
    if purchase_amount <= 0:
        print("Invalid purchase amount. Please enter a positive number.")
    else:
        # Apply discount based on payment method
        if payment_method == "cash" and purchase_amount > 100:
            discount_rate = 0.05
        elif payment_method == "credit card" and purchase_amount > 100:
            discount_rate = 0.02
        else:
            discount_rate = 0
        
        # Calculate final amount with discount
        if discount_rate > 0:
            discounted_amount = purchase_amount * (1 - discount_rate)
            print(f"Final amount: {discounted_amount:.2f} EUR")
        else:
            print(f"No discount applicable. Final amount: {purchase_amount:.2f} EUR")
except ValueError:
    print("Invalid input. Please enter a valid number for the purchase amount.")
```

### Explanation:

1. **Variable Initialization**: 
   - `purchase_amount` and `payment_method` are initialized as variables to simulate user input.

2. **Try-Except Block**:
   - The `try` block attempts to convert the `purchase_amount` to a float.
   - If the conversion is successful, it proceeds with further checks and calculations.
   - If there's a `ValueError`, it prints an error message indicating that the input is invalid.

3. **Conditional Statements**:
   - Checks if the `purchase_amount` is positive.
   - Depending on the `payment_method` ("cash" or "credit card") and whether the purchase amount exceeds 100 EUR, it applies the appropriate discount rate.
   - If no discount applies, it displays the original purchase amount.

4. **Discount Calculation**:
   - The final amount is calculated by applying the discount rate if applicable and prints the result.

### Example Test Cases:

- **Valid Input with Discount**:
  ```python
  purchase_amount = "150"
  payment_method = "cash"
  ```
  Output: `Final amount: 142.50 EUR`

- **Valid Input with No Discount**:
  ```python
  purchase_amount = "120"
  payment_method = "credit card"
  ```
  Output: `Final amount: 117.60 EUR`

- **Invalid Input**:
  ```python
  purchase_amount = "abc"
  payment_method = "cash"
  ```
  Output: `Invalid input. Please enter a valid number for the purchase amount.`

This code adheres to the constraints and requirements provided, using conditional statements and exception handling without loops or data structures.