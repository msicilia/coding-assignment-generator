```python
def calculate_change(price, paid):
    values = [500.0, 200.0, 100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    change = paid - price
    result = {}
    for value in values:
        if change >= value:
            count = int(change // value)
            result[value] = count
            change -= count * value
    return result
```