Let's break down this problem into smaller parts:

1. Take an input list of integers.
2. Create two empty lists for storing even and odd numbers.
3. Iterate through the input list, and for each number:
a. Check if it is even or odd.
b. If it is even, append it to the even list.
c. If it is odd, append it to the odd list.
4. Sort both lists in ascending order (even first) and descending order (odd first).
5. Return the two sorted lists as a tuple.

Here's the code:
```python
def sort_even_odd(numbers):
    even = []
    odd = []
    
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
            
    return (sorted(even), sorted(odd, reverse=True))
```
Test cases:

1. `sort_even_odd([])` should return `([], [])`.
2. `sort_even_odd([1, 2, 3])` should return `([1, 2], [3])`.
3. `sort_even_odd([1, 2, 3, 4])` should return `([1, 2], [3, 4])`.
4. `sort_even_odd([1, 2, 3, 4, 5])` should return `([1, 2, 4], [3, 5])`.

Note that we are using the built-in `sorted()` function to sort the lists in ascending and descending order respectively. We are also appending the numbers to the corresponding list based on their parity (even or odd).