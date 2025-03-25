Certainly! Below is the Python code that meets all the specified requirements:

```python
# Define variables for the test cases
purchase_amounts = [120.0, 80.0, '150', -30.0]

# Function to apply discount based on payment method and purchase amount
def apply_discount(purchase_amount, payment_method):
    try:
        # Convert purchase amount to float
        purchase_amount = float(purchase_amount)
        
        if purchase_amount <= 0:
            print("Invalid purchase amount. Please enter a positive number.")
            return None
        
        if payment_method == "cash":
            discount_rate = 0.05 if purchase_amount > 100 else 0
        elif payment_method == "credit card":
            discount_rate = 0.02
        else:
            print("Invalid payment method. Please choose either 'cash' or 'credit card'.")
            return None
        
        discounted_amount = purchase_amount * (1 - discount_rate)
        print(f"The final amount to pay is: {discounted_amount:.2f} EUR")
        return discounted_amount
    
    except ValueError:
        print("Invalid input. Please enter a valid number for the purchase amount.")
        return None

# Run test cases
for amount in purchase_amounts:
    apply_discount(amount, "cash")  # Test cash payment method
    apply_discount(amount, "credit card")  # Test credit card payment method
```

### Explanation:

1. **Variables and Function Definition**:
   - The `purchase_amounts` list contains several test cases for the purchase amount.
   - The `apply_discount` function takes two parameters: `purchase_amount` and `payment_method`.

2. **Input Validation**:
   - Inside the `try` block, the `purchase_amount` is converted to a float. If it fails (i.e., if the input is not a valid number), a `ValueError` will be caught.
   - The function checks if the `purchase_amount` is positive. If it's not, an error message is printed, and the function returns `None`.

3. **Discount Calculation**:
   - Depending on the `payment_method`, different discount rates are applied:
     - A 5% discount if the purchase amount is greater than 100 EUR when paid in cash.
     - A 2% discount for any payment made by credit card.
   - If an invalid `payment_method` is provided, an error message is printed.

4. **Output**:
   - The final discounted amount is printed using formatted string literals (`f-string`) to ensure it has two decimal places.

5. **Running Test Cases**:
   - The code runs through the test cases by calling the `apply_discount` function with both "cash" and "credit card" payment methods.

This code ensures that the requirements are met, including error handling for invalid inputs and applying discounts based on the specified conditions.