Thought: To solve this problem without using functions, we need to directly calculate the tax payable based on the given formula. The formula involves subtracting deductions from the annual income and then calculating one third of the result as the tax payable. We will use variables for the annual income and number of sons to compute the tax.

Code:
```py
annual_income = 50000  # Replace with actual annual income
number_of_sons = 2    # Replace with actual number of sons

taxable_income = annual_income - 600 - (60 * number_of_sons)
tax_payable = taxable_income / 3

print("Tax Payable:", tax_payable)
```