Here's how you can solve this problem using Python:

```python
def generate_lists(original_list):
    # Initialize empty lists for even and odd numbers
    even_nums = []
    odd_nums = []

    for num in original_list:
        if num % 2 == 0:  # Check if the number is even
            insert_in_order(even_nums, num)
        else:  # The number is odd
            insert_in_order(odd_nums, num, descending=True)

    return even_nums, odd_nums

def insert_in_order(lst, value, descending=False):
    for i in range(len(lst)):
        if (descending and lst[i] < value) or (not descending and lst[i] > value):
            lst.insert(i, value)
            return 
    lst.append(value)  # If the number is the smallest so far

```

To test this function:

```python
print(generate_lists([3,2,1,5,4,6]))  # Should return ([2, 4, 6], [5, 3, 1])
```