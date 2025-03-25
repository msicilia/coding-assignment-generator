 ```python
   # Assuming purchase_amount and payment_method are given variables for testing
   # For actual implementation replace them with input() function calls

   try:
       purchase_amount = float(purchase_amount)  # Try converting the input to float
       if purchase_amount > 100:
           if payment_method.lower() == 'cash':
               discounted_price = purchase_amount - (0.05 * purchase_amount)
           elif payment_method.lower() == 'credit card':
               discounted_price = purchase_amount - (0.02 * purchase_amount)
       else:
           discounted_price = purchase_amount  # No discount for purchase less than or equal to 100 EUR
   except ValueError:
       discounted_price = "Invalid input! Please enter a valid number."

   discounted_price
   ```