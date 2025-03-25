Here's an example solution in Python without using functions:
```python
# Define variables
euros = 100  # amount in euros (EUR)
exchange_rate = 0.84  # exchange rate of euro to pound sterling
commission = 0.02  # commission rate of the exchange house

# Calculate the equivalent amount in pounds sterling without commission
amount_no_commission = euros * exchange_rate

# Calculate the commission amount
commission_amount = amount_no_commission * commission

# Subtract the commission from the initial conversion to get final amount in GBP 
final_amount = amount_no_commission - commission_amount

print(f"The equivalent amount in pounds sterling after applying the commission is: {final_amount}")
```
This program starts by defining the amount of euros, the exchange rate from euro to pound sterling and the commission rate. Then it calculates the amount without the commission applied, the amount of the commission and finally subtracts the commission from the original conversion.