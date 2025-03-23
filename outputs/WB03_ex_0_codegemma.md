```python
# Define the purchase amount and payment method
purchase_amount = 120
payment_method = "cash"

# Check if the purchase amount is valid
try:
    purchase_amount = float(purchase_amount)
except ValueError:
    print("Invalid purchase amount. Please enter a valid number.")
    exit()

# Calculate the discount and total amount
if purchase_amount > 100 and payment_method == "cash":
    discount = 0.05 * purchase_amount
elif purchase_amount > 100 and payment_method == "credit card":
    discount = 0.02 * purchase_amount
else:
    discount = 0

total_amount = purchase_amount - discount

# Print the total amount
print("Total amount:", total_amount)
```

**Explanation:**

* The code defines the purchase amount and payment method as variables.
* It uses a `try-except` block to check if the purchase amount is a valid number. If not, it prints an error message and exits the program.
* Based on the purchase amount and payment method, it calculates the discount and total amount using conditional statements.
* Finally, the code prints the total amount.

**Note:**

* The code does not use any data structures, loops, or match expressions as specified in the task.
* The example test case provided in the task is not included in the solution.