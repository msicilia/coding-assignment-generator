Here's an example Python code that will perform the conversion from Euro to Pound Sterling (GBP) accounting for a 2% commission:

```python
# Define the variables
eur = 100  # Amount in Euros
exchange_rate = 0.85  # Exchange rate from Euro to GBP as of the day
commission = 0.02  # Commission percentage

# Calculate the total including commission
total_including_commission = eur * (1 + commission)

# Convert to GBP using exchange rate
gbp = total_including_commission * exchange_rate

print(f'The equivalent amount in Pound Sterling taking into account the commission is: {gbp}')
```