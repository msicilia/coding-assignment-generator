
Here's an example code that solves the problem you described, without using data structures or loops:
```python
purchase_amount = input("Enter the amount of your purchase: ")
try:
    float(purchase_amount)
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()
if float(purchase_amount) > 100:
    if payment_method == "Cash":
        discount = 0.05 * float(purchase_amount)
    else:
        discount = 0.02 * float(purchase_amount)
else:
    discount = 0
print(f"The discount is {discount} EUR.")
```
This code first asks the user to input the amount of their purchase, and then checks if the input is a valid number using the `try`/`except` block. If the input is not a valid number, it prints an error message and exits the program. If the input is valid, it proceeds with calculating the discount based on the payment method.

The code uses conditional statements to check if the purchase amount is greater than 100, and applies the appropriate discount rate accordingly. It then prints the calculated discount using string formatting.

Note that this code does not use any data structures or loops, which are not allowed in the problem statement. However, it does use the `try`/`except` block to handle errors and the `float()` function to convert the input to a floating-point number.