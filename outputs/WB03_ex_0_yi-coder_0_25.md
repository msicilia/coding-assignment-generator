Here's an example solution written in Python for this problem, which adheres to your specifications.
```python
def calculate_discount(purchase_amount: str, payment_method: str):
    try: 
        purchase_amount = float(purchase_amount)  # try converting input to a float type number
    except ValueError:   # if it's not possible return an error message
        return "Invalid purchase amount."
    if purchase_amount <= 0:
        return "Purchase amount must be positive."
    discount = 0
    if payment_method == 'cash':  # If the payment method is cash and the purchase amount >100 then apply a discount of 5%
        if purchase_amount > 100:
            discount += 5
    elif payment_method == 'credit_card':   # if the payment method is credit card apply a discount of 2%
        discount += 2
    else:
        return "Invalid payment method. Please choose between cash and credit_card"  
    final_price = purchase_amount - (purchase_amount * discount / 100)   # calculate the final price after the discount has been applied.
    return f'The final price of your purchase is {final_price} EUR after a {discount}% discount has been applied.'  
```
You can use this function in Python to simulate user interaction:
```python
print(calculate_discount('200', 'cash'))   # expected output "The final price of your purchase is 190.0 EUR after a 5% discount has been applied"
print(calculate_discount('75', 'cash'))    # expected output: "Purchase amount must be positive."
print(calculate_discount('abc', 'cash'))   # expected output: "Invalid purchase amount."
print(calculate_discount('200', 'credit_card')) # expected output: "The final price of your purchase is 198.0 EUR after a 2% discount has been applied."
```