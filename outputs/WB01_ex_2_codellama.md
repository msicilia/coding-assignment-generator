 
Here's an example solution for the problem:
```py
# Calculate the tax payable based on the annual income and number of sons
def calculate_tax(annual_income, num_sons):
    # Calculate the total income minus the personal deduction
    total_income = annual_income - 600
    
    # Calculate the tax payable as one third of the total income
    tax_payable = total_income / 3
    
    # Add the deduction for each son
    for i in range(num_sons):
        tax_payable += 60
    
    return tax_payable
```
Example test cases:
```py
# Test case 1: Basic calculation
assert calculate_tax(5000, 2) == 1500

# Test case 2: Multiple sons
assert calculate_tax(6000, 3) == 2000

# Test case 3: No sons
assert calculate_tax(7000, 0) == 2166.6666666666668
```