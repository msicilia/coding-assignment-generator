 To solve this problem, we can use conditional statements and try-except blocks in Python as per your requirements. Here's an example of how you might write the code:

```python
# Variables to represent the purchase amount and payment method
purchase_amount = '120'  # This could be any string representing a number
payment_method = 'cash'  # This could be either 'cash' or 'credit card'

try:
    # Try to convert the purchase amount to a float
    purchase_amount = float(purchase_amount)
except ValueError:
    print("Invalid input for purchase amount. Please enter a number.")
else:
    # If the conversion was successful, proceed with calculations
    if purchase_amount > 100:
        if payment_method == 'cash':
            final_price = purchase_amount * 0.95  # Apply 5% discount
        elif payment_method == 'credit card':
            final_price = purchase_amount * 0.98  # Apply 2% discount
        else:
            print("Invalid input for payment method. Please enter either 'cash' or 'credit card'.")
    else:
        final_price = purchase_amount  # No discount applied
    print(f"The final price is {final_price} EUR.")
```

In this code, `purchase_amount` and `payment_method` are variables that represent the input data. We use a try-except block to attempt to convert `purchase_amount` to a float. If this conversion fails (for example, if `purchase_amount` is not a number), we print an error message and exit the program.

If the conversion is successful, we check whether `purchase_amount` is greater than 100 EUR. If it is, we apply a discount based on the `payment_method`. We then calculate the final price and print it.