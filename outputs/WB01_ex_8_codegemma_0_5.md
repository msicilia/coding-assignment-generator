```python
# Define the basic salary and commission rate
basic_salary = 2000
commission_rate = 0.03
income_tax_rate = 0.32

# Define the total sales made by the salesperson
total_sales = 100000

# Calculate the commission
commission = total_sales * commission_rate

# Calculate the net salary before tax
net_salary_before_tax = basic_salary + commission

# Calculate the income tax
income_tax = net_salary_before_tax * income_tax_rate

# Calculate the net salary
net_salary = net_salary_before_tax - income_tax

# Print the net salary
print("The net salary of the salesperson is:", net_salary, "euros")
```