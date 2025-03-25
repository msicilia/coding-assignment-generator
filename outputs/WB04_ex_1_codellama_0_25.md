Sounds like a fun challenge! Here's my solution:
```
def get_change(total, amount):
    change = total - amount
    coins = []
    for coin in (500.0, 200.0, 100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01):
        if change >= coin:
            coins.append(coin)
            change -= coin
    return coins
```
This function takes two arguments: `total` and `amount`. It calculates the difference between the total and amount paid by the customer, and then iterates over a list of coin values to determine how many coins are needed for change. The resulting coins are returned as a list.

Here's an example usage:
```
>>> get_change(100.0, 50.0)
[50.0]
```
This function can be used to calculate the change for any value of `total` and `amount`, as long as the coin values are consistent with the currency in use.