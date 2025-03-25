Here is an answer for the user task:
You are a Python instructor in an introduction to programming course at graduate level.
 
Write Python code to solve the following problem:
Write a code that calculates the tax payable by a taxpayer based on his annual income and number of sons. The tax payable is one third of the taxable income, the latter being equal to the total income minus a personal deduction of €600 and a further deduction of €60 per son.

You cannot use the following Python elements:
functions

You must use the following Python elements:
No required elements

When writing some example test cases take into account the following:
No test case hints

Take into account the following additional requirements:
Do not use calls to input() to read data from the keyboard. Use variables instead to exercise the code.

Here is an example of a solution to the problem:
```
# Define variables for annual income and number of sons
income = 100000
sons = 2

# Calculate taxable income
taxable_income = income - 600 - 60 * sons

# Calculate tax payable
tax = taxable_income / 3

# Print the result
print(tax)
```
This code uses variables to store the annual income and number of sons, calculates the taxable income by subtracting the personal deductions, and then calculates the tax payable by dividing the taxable income by three. Finally, it prints the result using the `print()` function.Note that this is just an example solution, and there may be other ways to solve the problem depending on the specific requirements of the task.