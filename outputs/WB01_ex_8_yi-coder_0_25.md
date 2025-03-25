Here is your solution:

```python
def calculateSalary(totalSales):
    basicSalary = 2000
    commissionRate = 3 / 100
    taxRate = 32 / 100

    commission = totalSales * commissionRate  # Calculate commission.
    salaryBeforeTax = basicSalary + commission  # Add the salary and the commission.
    netSalary = salaryBeforeTax * (1 - taxRate) # Subtract the tax from the salary.

    return netSalary
```