To solve this problem within the constraints provided, we can use basic data types and conditional statements along with `try-except` blocks. Below is a Python code snippet that meets all the requirements:

```python
# Simulated user input (replace this with actual input handling in your environment)
purchase_amount_str = "150"  # This should be replaced by an actual input from the seller
payment_method = "cash"      # This should be replaced by an actual input from the seller

try:
    # Convert purchase amount to float
    purchase_amount = float(purchase_amount_str)

    # Check if the purchase amount is greater than 100 EUR
    if purchase_amount > 100:
        # Apply discount based on payment method
        if payment_method == "cash":
            discount_rate = 0.05
        elif payment_method == "credit_card":
            discount_rate = 0.02
        else:
            raise ValueError("Invalid payment method")

        # Calculate the discounted amount
        discounted_amount = purchase_amount * (1 - discount_rate)
        print(f"Final amount after discount: {discounted_amount:.2f} EUR")
    else:
        print("No discount applied, total is the same.")

except ValueError as e:
    # Handle invalid input
    print(f"Error: {e}")
    print("Please enter a valid number for the purchase amount.")
```

### Explanation:

1. **Input Handling**:
   - The `purchase_amount_str` and `payment_method` variables are used to simulate user inputs.
   - In a real-world scenario, these values should be obtained from the user using appropriate input methods.

2. **Validation with `try-except` Block**:
   - The code attempts to convert the `purchase_amount_str` to a float.
   - If the conversion is successful, it proceeds to check if the purchase amount is greater than 100 EUR.
   - Depending on the payment method (`cash` or `credit_card`), it applies the corresponding discount rate and calculates the discounted amount.

3. **Conditional Statements**:
   - The code uses conditional statements (`if`, `elif`, `else`) to handle different scenarios, such as valid input, invalid input, and different payment methods.
   - If the payment method is not recognized, it raises a `ValueError`.

4. **Output Handling**:
   - The final discounted amount is printed if the conditions are met.
   - If the purchase amount is not a valid number or the payment method is invalid, appropriate error messages are displayed.

This code snippet ensures that the requirements are met without using any data structures, loops, or match expressions, adhering to the constraints provided.