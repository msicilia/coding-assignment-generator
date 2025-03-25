Here is a Python function that solves the problem:

```python
def calculate_change(price, paid):
    change = {}
    coins = [500.0, 200.0, 100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    remaining = paid - price
    for coin in coins:
        if remaining >= coin:
            count = int(remaining // coin)
            remaining -= count * coin
            change[coin] = count
    return {k: v for k, v in change.items() if v != 0}
```
The function `calculate_change` takes two parameters - the price of the product and the amount paid by the customer. Then it calculates how much money is remaining to be given as change. The variable 'coins' stores the available types of coins in euros, starting from the highest value (500.0) down to the smallest (0.01). The function then iterates over these coin values and checks if there are any whole coins that can be returned as a change. If so, it subtracts this amount from the remaining balance and adds an entry in the 'change' dictionary for this type of coin. Finally, the function returns a dictionary with only non-zero counts.