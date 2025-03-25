```python
# Define the amount in euros
amount_euros = 120

# Define the exchange rate
exchange_rate = 0.84

# Define the commission percentage
commission = 0.02

# Calculate the amount in pounds before commission
amount_pounds_before_commission = amount_euros * exchange_rate

# Calculate the commission amount
commission_amount = amount_pounds_before_commission * commission

# Calculate the amount in pounds after commission
amount_pounds = amount_pounds_before_commission - commission_amount

# Print the results
print("Amount in Euros:", amount_euros)
print("Exchange Rate:", exchange_rate)
print("Commission:", commission)
print("Amount in Pounds:", amount_pounds)
```