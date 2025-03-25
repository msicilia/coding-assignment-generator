Here's how you might solve this problem using Python:

```python
# Variables that represent the income and number of sons for the person. 
# Change these values to test different scenarios.
annual_income = 12000
number_of_sons = 3

# Calculate the taxable income by subtracting the personal deduction and the son's deductions from the total income.
taxable_income = annual_income - 600 - (number_of_sons * 60)

# Calculate the tax payable by taking one third of the taxable income.
tax_payable = taxable_income / 3

print('The tax payable is:', tax_payable)
```
In this code snippet, we first define the annual income and number of sons for a particular person. Then, we calculate the taxable income by subtracting both the personal deduction (600€) and the son's deductions from the total income. After that, to find out the tax payable amount, we divide the taxable income by 3. Finally, we print this calculated tax amount on the screen.