Here is the Python code that calculates the tax payable by a taxpayer based on his annual income and number of sons, following the given requirements:

```py
# Input values
annual_income = 50000  # Example annual income in euros
number_of_sons = 2    # Example number of sons

# Calculate taxable income
taxable_income = annual_income - 600 - (60 * number_of_sons)

# Calculate tax payable
tax_payable = taxable_income / 3

# Print the result
print("Tax Payable:", tax_payable)
```

This code calculates the tax payable by first determining the taxable income, which is the annual income minus a personal deduction of €600 and a further deduction of €60 per son. Then, it calculates the tax payable as one third of the taxable income and prints the result.

You can modify the values of `annual_income` and `number_of_sons` to test different scenarios.