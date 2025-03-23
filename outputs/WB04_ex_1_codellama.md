  To solve this problem, we need to design a function that takes two arguments: the total amount of money and the payment made by the customer. The function should return the number of coins and bills needed as change, without specifying any quantities for which there would be zero units.

Here is an example implementation of such a function in Python:
```
def get_change(total, payment):
    # Calculate the difference between the total amount and the payment
    change = total - payment
    
    # Initialize an empty list to store the coins and bills
    coins = []
    bills = []
    
    # Iterate over the denominations of money in the country
    for denomination in [500.0, 200.0, 100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]:
        # Calculate the number of coins and bills needed for this denomination
        num_coins = int(change / denomination)
        num_bills = change % denomination
        
        # Add the coins and bills to the lists
        if num_coins > 0:
            coins.append(num_coins)
        if num_bills > 0:
            bills.append(num_bills)
    
    # Return the list of coins and bills
    return coins + bills
```
This function first calculates the difference between the total amount and the payment made by the customer. It then iterates over the denominations of money in the country, calculating the number of coins and bills needed for each denomination using integer division and modulo operations. Finally, it returns the list of coins and bills as change.

For example, if we call the function with total = 1500.0 and payment = 100.0, it would return the following list:
```
[200.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.2, 0.1]
```
This indicates that the cashier should give the customer two bills of 200.0, five coins of 50.0, and so on.