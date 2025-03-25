Here's one way you could write this in Python. This program uses variables instead of calls to `input()` to read data from the keyboard, and only uses conditional statements and try-except blocks:
```python
def calculate_discount(purchase_amount, is_cash):
    try:
        float_purchase_amount = float(purchase_amount)
    except ValueError:
        return "Invalid purchase amount"

    if float_purchase_amount > 100 and is_cash:
        discount = float_purchase_amount * 5 / 100  # 5% discount if paid in cash for purchases over 100EUR.
    elif float_purchase_amount <= 100 and is_cash:
        discount = float_purchase_amount * 2 / 100  # 2% discount if paid in cash for purchases up to or equal to 100EUR.
    else:
        discount = float_purchase_amount * 2 / 100  # 2% discount if payment is by credit card.

    return discount

# Example usage:
purchase_amount = "150"   # Replace this with real user input or another form of data entry.
is_cash = True            # Replace this with real user input or another form of data entry.
discount = calculate_discount(purchase_amount, is_cash)
print('The discount for the purchase amount {} is {}'.format(purchase_amount, discount))
```