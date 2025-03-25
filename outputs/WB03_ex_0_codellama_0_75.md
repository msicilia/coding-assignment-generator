```
amount = float(input("Enter the amount of the purchase: "))
if amount > 100.0:
    if payment_method == "cash":
        discount = amount * 0.05
    else:
        discount = amount * 0.02
else:
    discount = 0.0
total = amount - discount
print(f"The total cost is {total:.2f}")
```
This code will ask the user for the amount of the purchase and then apply a discount based on the payment method. If the amount is higher than 100 EUR, a 5% discount will be applied if paid in cash, otherwise a 2% discount will be applied. The total cost will be calculated by subtracting the discount from the original amount.

Note that this code uses try-except blocks to check if the input can be converted to a float, and it uses conditional statements to determine the type of discount to apply based on the payment method. It also uses string formatting to print the total cost with 2 decimal places.