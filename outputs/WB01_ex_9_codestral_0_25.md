 Thought: I will convert the given Euro amount to Pounds by multiplying it with the exchange rate and then subtracting the commission.

   Code:
   ```python
   euros = 100
   exchange_rate = 0.85
   total_pounds = euros * exchange_rate
   commission = total_pounds * 0.02
   final_amount = total_pounds - commission
   print(final_amount)
   ```