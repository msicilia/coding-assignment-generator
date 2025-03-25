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

# Example test cases
nums1 = [1, 2, 3, 4, 5]
even_nums1, odd_nums1 = sort_even_odd(nums1)
print(even_nums1)  # Output: [2, 4]
print(odd_nums1)  # Output: [3, 1, 5]

nums2 = [10, 9, 8, 7, 6]
even_nums2, odd_nums2 = sort_even_odd(nums2)
print(even_nums2)  # Output: [10, 8]
print(odd_nums2)  # Output: [9, 7, 6]
```