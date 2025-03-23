```python
def calculate_discount(purchase_amount, is_cash):
    try:
        float_amount = float(purchase_amount)
    except ValueError:
        return "Invalid purchase amount"

    if float_amount > 100 and is_cash:
        discount = float_amount * 5 / 100
    elif float_amount > 100 and not is_cash:
        discount = float_amount * 2 / 100
    else:
        discount = 0

    return discount

# Test cases
print(calculate_discount("200", True)) # Should print 10.0 as a 5% discount is applied if the purchase amount is higher than 100EUR and paid in cash
print(calculate_discount("300", False)) # Should print 6.0 as a 2% discount is applied if the purchase amount is higher than 100EUR and paid by credit card
print(calculate_discount("50", True))  # Should print 0 as no discount should be applied if the purchase amount is lower or equal to 100EUR
```