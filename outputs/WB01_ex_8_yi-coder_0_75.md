```python
# Define constants for readability
basic_salary = 2000  # euros per month
commission_rate = 3   # in percentage
tax_rate = 32         # in percentage

sales_data = [2500, 3800, 4200] # example data
for sales in sales_data:
    total_income = basic_salary + (sales * commission_rate / 100)
    net_income = total_income - (total_income * tax_rate / 100)
    print("Net salary for sales of", sales, "euros:", net_income, "euros")
```