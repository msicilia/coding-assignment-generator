To write this code, you can use a conditional statement to check if the purchase amount is greater than 100 EUR. If it is, you can apply a discount of either 5% or 2%, depending on whether the payment was made by cash or credit card. Here's an example of how this code could look:
```
purchase_amount = float(input("Enter the amount of your purchase: "))
if purchase_amount > 100:
    if input("Did you pay with cash? (y/n): ") == "y":
        discount = purchase_amount * 0.05
    else:
        discount = purchase_amount * 0.02
else:
    discount = 0
total = purchase_amount - discount
print(f"The total cost of your purchase is {total} EUR.")
```
This code uses a try-except block to check if the input can be converted to a float, and if it cannot, it will print an error message and ask the user to enter a valid number again. This ensures that only valid inputs are used in the calculations.

You can also use the `float()` function to convert the input to a float, and then check if it is greater than 100 EUR. Here's an example of how this code could look:
```
while True:
    try:
        purchase_amount = float(input("Enter the amount of your purchase: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
if purchase_amount > 100:
    if input("Did you pay with cash? (y/n): ") == "y":
        discount = purchase_amount * 0.05
    else:
        discount = purchase_amount * 0.02
else:
    discount = 0
total = purchase_amount - discount
print(f"The total cost of your purchase is {total} EUR.")
```
This code uses a `while` loop to keep asking the user for input until they enter a valid number. It then uses the `float()` function to convert the input to a float, and checks if it is greater than 100 EUR. If it is, it applies the appropriate discount, otherwise it sets the discount to 0. Finally, it calculates the total cost of the purchase and prints it out.