```python
purchase_amount = 120  # Example purchase amount
payment_method = "cash"  # Example payment method

try:
    purchase_amount = float(purchase_amount)
except ValueError:
    print("Invalid purchase amount. Please enter a valid number.")
else:
    if purchase_amount > 100:
        if payment_method == "cash":
            discount = 0.05 * purchase_amount
        else:
            discount = 0.02 * purchase_amount
        total_amount = purchase_amount - discount
        print("Total amount with discount:", total_amount)
    else:
        print("No discount applied. Total amount:", purchase_amount)
```

**Explanation:**

* The code includes the payment method variable, which is defined as "cash" for the example.
* The code uses a try-except block to check that the purchase amount can be converted to a float.
* If the purchase amount is valid, the code calculates the discount based on the payment method and the purchase amount.
* The code then calculates the total amount with the discount and prints it to the console.

**Output:**

```
Total amount with discount: 114.0
```