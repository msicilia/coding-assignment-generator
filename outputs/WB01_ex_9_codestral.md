 Code:
   ```python
   # Define variables with sample values
   euros = 100
   exchange_rate = 0.85

   # Calculate total amount in GBP without commission
   gbp_total = euros * exchange_rate

   # Calculate the commission amount (2% of the total)
   commission = 0.02 * gbp_total

   # Subtract the commission from the total to get the equivalent in GBP
   gbp_equivalent = gbp_total - commission

   print("The equivalent amount in Pounds Sterling (GBP) is:", gbp_equivalent)
   ```