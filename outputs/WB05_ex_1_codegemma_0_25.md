```python
def sort_even_odd(nums):
    even_nums = []
    odd_nums = []

    for num in nums:
        if num % 2 == 0:
            # Find the insertion point for even numbers
            i = 0
            while i < len(even_nums) and even_nums[i] < num:
                i += 1
            even_nums.insert(i, num)
        else:
            # Find the insertion point for odd numbers
            i = 0
            while i < len(odd_nums) and odd_nums[i] > num:
                i += 1
            odd_nums.insert(i, num)

    return even_nums, odd_nums
```

**Example Usage:**

```python
nums = [5, 2, 8, 3, 7, 1]
even_nums, odd_nums = sort_even_odd(nums)

print("Even numbers:", even_nums)  # Output: [2, 8]
print("Odd numbers:", odd_nums)   # Output: [7, 5, 3, 1]
```

**Explanation:**

* The function iterates over the original list `nums`.
* For each number, it checks if it is even or odd.
* If the number is even, it finds the insertion point in the `even_nums` list using a `while` loop and inserts the number.
* If the number is odd, it finds the insertion point in the `odd_nums` list using a `while` loop and inserts the number.
* The function returns both the `even_nums` and `odd_nums` lists.

**Note:**

* The `while` loops ensure that the numbers are inserted in sorted order in the respective lists.
* The code does not use `match expressions` or `list comprehensions` as required.