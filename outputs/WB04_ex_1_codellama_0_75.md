  Sure, here's an example solution to the problem:
```
def change(amount_paid, amount):
    bills = [500.0, 200.0, 100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    coins = [0.50, 0.25, 0.10, 0.05, 0.01]
    
    bill_count = 0
    coin_count = 0
    
    while amount > 0:
        if amount >= bills[bill_count]:
            amount -= bills[bill_count]
            bill_count += 1
        else:
            coin_count += int(amount / coins[coin_count])
            break
    
    return (bill_count, coin_count)
```
This function takes two arguments: `amount_paid` and `amount`. It returns a tuple containing the number of bills and coins that should be given as change. The function uses a loop to iterate over the different bill denominations and checks if the current amount is greater than or equal to the current bill denomination. If it is, then it subtracts the bill denomination from the amount and increments the `bill_count` variable. If it's not, then it divides the amount by the corresponding coin denomination and rounds down to the nearest integer to determine the number of coins that should be given as change. The loop continues until the amount is 0 or less.

Here are some example test cases for this function:
```
# Test case 1: Change for a $5 purchase with a $5 bill and no coins
assert change(5, 5) == (1, 0)

# Test case 2: Change for a $2.50 purchase with a $5 bill and 2 coins
assert change(2.50, 5) == (1, 2)

# Test case 3: Change for a $2.50 purchase with a $2.50 bill and no coins
assert change(2.50, 2.50) == (1, 0)

# Test case 4: Change for a $2.50 purchase with a $1 bill and 2 coins
assert change(2.50, 1) == (1, 2)

# Test case 5: Change for a $2.50 purchase with a $1 bill and 3 coins
assert change(2.50, 1) == (1, 3)
```