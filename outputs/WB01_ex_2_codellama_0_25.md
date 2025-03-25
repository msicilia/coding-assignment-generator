Let's start by breaking down the problem into smaller parts. We need to calculate the taxable income, which is the total income minus the personal deduction of €600 and the further deduction of €60 per son. Then we can calculate the tax payable as one third of the taxable income.

Here's an example code:
```
income = 50000
sons = 2

# Calculate taxable income
taxable_income = income - (600 + 60 * sons)

# Calculate tax payable as one third of the taxable income
tax_payable = taxable_income / 3

print(f"The tax payable is {tax_payable}.")
```
This code calculates the tax payable for a taxpayer with an annual income of €50,000 and two sons. The output should be "The tax payable is €16,667."