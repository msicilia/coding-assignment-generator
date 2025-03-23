Here is a Python code which solves the problem:

```python
# The total sales made by the salesperson in the last month
total_sales = 3000  # replace with actual value or another variable as required

# Constants defined
basic_salary = 2000
commission_rate = 0.03
income_tax_rate = 0.32

# Calculate the gross salary including commission on total sales made
gross_salary = basic_salary + (total_sales * commission_rate)

# Deduct income tax and find net salary to be received
net_salary = gross_salary - (gross_salary * income_tax_rate)

print("The net salary the salesperson will receive is: ", net_salary)
```