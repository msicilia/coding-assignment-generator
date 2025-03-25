```python
purchase_amount = 120  # Example purchase amount
payment_method = "cash"  # Example payment method

try:
    purchase_amount = float(purchase_amount)  # Check if the input can be converted to a float

    if purchase_amount > 100:
        if payment_method == "cash":
            discount = 0.05 * purchase_amount
        else:
            discount = 0.02 * purchase_amount

        total_amount = purchase_amount - discount

        print("Total amount with discount:", total_amount)

except ValueError:
    print("Invalid purchase amount. Please enter a valid number.")
```