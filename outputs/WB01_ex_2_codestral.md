 ```python
# Test case 1: Annual income = €8000, Number of sons = 2
annual_income_1 = 8000
number_of_sons_1 = 2
personal_deduction = 600
son_deduction = 60
taxable_income_1 = annual_income_1 - personal_deduction - (number_of_sons_1 * son_deduction)
tax_payable_1 = taxable_income_1 / 3
print("Test case 1: Tax payable = ", tax_payable_1)

# Test case 2: Annual income = €4500, Number of sons = 1
annual_income_2 = 4500
number_of_sons_2 = 1
taxable_income_2 = annual_income_2 - personal_deduction - (number_of_sons_2 * son_deduction)
tax_payable_2 = taxable_income_2 / 3
print("Test case 2: Tax payable = ", tax_payable_2)
```
The above code calculates the tax payable for two test cases based on the given conditions. The tax payable is calculated by first determining the taxable income (total income minus personal deduction and son deductions), and then dividing that by three to obtain the tax payable amount.