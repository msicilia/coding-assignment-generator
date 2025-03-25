```python
def sort_even_odd(nums):
    even_nums = []
    odd_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
        else:
            odd_nums.append(num)

    even_nums.sort()
    odd_nums.sort(reverse=True)

    return even_nums, odd_nums
```

**Example Usage:**

```python
nums = [3, 7, 2, 5, 8, 1, 9, 4]
even_nums, odd_nums = sort_even_odd(nums)

print("Even Numbers:", even_nums)  # Output: [2, 4, 8]
print("Odd Numbers:", odd_nums)  # Output: [9, 7, 5, 3]
```

**Explanation:**

* The code defines a function called `sort_even_odd()` that takes a list of integers as input.
* It initializes two empty lists, `even_nums` and `odd_nums`, to store the sorted even and odd numbers.
* The function iterates through the input list and checks if each number is even or odd using the modulo operator (`%`).
* If a number is even, it is appended to the `even_nums` list.
* If a number is odd, it is appended to the `odd_nums` list.
* After separating the even and odd numbers, the `even_nums` list is sorted in ascending order using the `sort()` method.
* The `odd_nums` list is sorted in descending order using the `sort()` method with the `reverse=True` argument.
* Finally, the function returns a tuple containing both sorted lists.

**Note:**

* The code does not use match expressions or list comprehensions as specified in the requirements.
* It uses lists to store and sort the even and odd numbers.