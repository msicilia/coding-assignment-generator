Here's an example code using variables instead of input() to read data from the keyboard:

```python
# Define variables for amount in euros and the exchange rate
amount_eur = 100  # Change this value as required
exchange_rate = 0.85  # Change this value as required

# Calculate the amount in GBP, including a commission of 2%
amount_gbp = (amount_eur * exchange_rate) * 0.98

print("The equivalent in GBP is:", amount_gbp)
```