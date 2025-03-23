```python
# Define variables for annual income and number of sons
annual_income = 50000  # Example value, can be changed
number_of_sons = 2    # Example value, can be changed

# Calculate the taxable income
taxable_income = annual_income - 600 - (60 * number_of_sons)

# Calculate the tax payable
tax_payable = taxable_income / 3

# Print the tax payable
print("Tax Payable:", tax_payable)
```

Explanation:
1. **Variables**: `annual_income` and `number_of_sons` are defined with example values.
2. **Taxable Income Calculation**:
   - The personal deduction is €600, so it is subtracted from `annual_income`.
   - A further deduction of €60 per son is calculated by multiplying `number_of_sons` by 60 and then subtracting this from the intermediate result.
3. **Tax Payable Calculation**:
   - The tax payable is one third of the taxable income, so it is divided by 3.
4. **Output**: The final tax payable amount is printed.

This code snippet adheres to the requirements by using only basic Python syntax and not employing any functions or input methods.