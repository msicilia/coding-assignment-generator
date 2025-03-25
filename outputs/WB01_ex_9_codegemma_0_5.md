```python
# Set the amount in euros and the exchange rate
euros = 500
exchange_rate = 0.82

# Calculate the amount in pounds without commission
pounds_without_commission = euros * exchange_rate

# Calculate the commission amount
commission = 0.02 * (pounds_without_commission)

# Calculate the amount in pounds with commission
pounds_with_commission = pounds_without_commission - commission

# Print the result
print("Amount in pounds with commission:", pounds_with_commission)
```