```python
def calculate_change(total, payment):
    coins = {500.0: 0, 200.0: 0, 100.0: 0, 50.0: 0, 20.0: 0, 10.0: 0, 5.0: 0,
              2.0: 0, 1.0: 0, 0.5: 0, 0.2: 0, 0.1: 0, 0.05: 0, 0.02: 0, 0.01: 0}
    change = payment - total
    for coin in sorted(coins.keys(), reverse=True):  # start from the highest coin value
        while change >= coin:                       # while enough money for the current coin is available
            coins[coin] += 1                      # increment that coin's count
            change -= coin                         # decrease the remaining change due to this coin
    return {k: v for k, v in coins.items() if v > 0}  # return only the coins which have a positive count

print(calculate_change(13.47, 20))   # example usage
```