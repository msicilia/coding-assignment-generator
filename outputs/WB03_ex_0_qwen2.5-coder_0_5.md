To solve this problem without using loops, match expressions, or data structures, we can use conditional statements and try-except blocks effectively. Here's the Python code:

```python
def apply_discount(purchase_amount, payment_method):
    if payment_method == "cash":
        discount = 0.05
    elif payment_method == "credit card":
        discount = 0.02
    else:
        print("Invalid payment method")
        return None

    discounted_amount = purchase_amount * (1 - discount)
    return discounted_amount

# Simulate input from the seller
try:
    purchase_amount = float(input("Enter the amount of the purchase: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
else:
    payment_method = input("Enter the payment method (cash/credit card): ")
    
    if purchase_amount > 100:
        discounted_amount = apply_discount(purchase_amount, payment_method)
        if discounted_amount is not None:
            print(f"Discounted amount: {discounted_amount:.2f} EUR")
    else:
        print("No discount applicable for purchases below or equal to 100EUR.")
```

### Explanation:

1. **Function `apply_discount`**:
   - This function takes two parameters: `purchase_amount` and `payment_method`.
   - It checks the payment method and applies the corresponding discount (5% for cash, 2% for credit card).
   - If an invalid payment method is provided, it prints an error message and returns `None`.

2. **Input Handling**:
   - The code attempts to convert the input for purchase amount to a float using a try-except block.
   - If the conversion fails, it prints an error message indicating that the input must be a valid number.
   - If the conversion is successful, it prompts the seller to enter the payment method.

3. **Conditional Logic**:
   - If the purchase amount is greater than 100 EUR, the code calls `apply_discount` with the purchase amount and payment method.
   - If the discount calculation is successful (i.e., `discounted_amount` is not `None`), it prints the discounted amount formatted to two decimal places.
   - If the purchase amount is 100 EUR or less, it prints a message indicating that no discount is applicable.

This code meets all the requirements specified in the problem statement, including the use of conditional statements and try-except blocks.