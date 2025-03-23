
Here is an example of how to solve this problem using variables instead of input() function:
```
# Define the exchange rate and the commission percentage
exchange_rate = 1.25 # EUR/GBP
commission_percentage = 0.02 # 2%

# Calculate the total amount after applying the commission
total = euros * exchange_rate - (euros * exchange_rate) * commission_percentage

# Print the result
print("The equivalent in pounds is", round(total, 2))
```
This program defines two constants: the exchange rate and the commission percentage. It then calculates the total amount after applying the commission using the formula `total = euros * exchange_rate - (euros * exchange_rate) * commission_percentage`. Finally, it prints the result with two decimal places using the round() function.

Note that this program does not use any input() function to read data from the keyboard. Instead, it uses variables to exercise the code and shows the equivalent in pounds for a given amount of euros and exchange rate.