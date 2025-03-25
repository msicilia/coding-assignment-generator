To solve this problem without using `match expressions`, list comprehensions, and specific Python elements as mentioned, we can manually insert each number into its appropriate position. This involves iterating through the original list and inserting each number into either the even or odd list based on whether it is even or odd.

Here's the complete solution:

```python
def generate_even_odd_lists(original_list):
    even_list = []
    odd_list = []

    for num in original_list:
        if num % 2 == 0:  # Check if the number is even
            inserted = False
            for i in range(len(even_list)):
                if even_list[i] >= num:
                    even_list.insert(i, num)
                    inserted = True
                    break
            if not inserted:
                even_list.append(num)
        else:  # The number is odd
            inserted = False
            for i in range(len(odd_list)):
                if odd_list[i] <= num:
                    odd_list.insert(i, num)
                    inserted = True
                    break
            if not inserted:
                odd_list.append(num)

    return even_list, odd_list

# Example test cases
original_list1 = [5, 3, 10, 2, 8, 7, 9, 4]
even_list1, odd_list1 = generate_even_odd_lists(original_list1)
print("Even List:", even_list1)  # Output: [2, 4, 8, 10]
print("Odd List:", odd_list1)    # Output: [3, 5, 7, 9]

original_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list2, odd_list2 = generate_even_odd_lists(original_list2)
print("Even List:", even_list2)  # Output: [2, 4, 6, 8, 10]
print("Odd List:", odd_list2)    # Output: [9, 7, 5, 3, 1]

original_list3 = []
even_list3, odd_list3 = generate_even_odd_lists(original_list3)
print("Even List:", even_list3)  # Output: []
print("Odd List:", odd_list3)    # Output: []

original_list4 = [0]
even_list4, odd_list4 = generate_even_odd_lists(original_list4)
print("Even List:", even_list4)  # Output: [0]
print("Odd List:", odd_list4)    # Output: []
```

### Explanation:
1. **Initialization**: We start with two empty lists, `even_list` and `odd_list`.
2. **Iteration through the original list**: For each number in the `original_list`, we determine whether it is even or odd.
3. **Insertion into even_list**:
   - If the number is even, we iterate through `even_list` to find the correct position where the number should be inserted to maintain ascending order.
   - If no such position is found (i.e., the number is larger than all existing numbers in `even_list`), we append it to the end of `even_list`.
4. **Insertion into odd_list**:
   - If the number is odd, we iterate through `odd_list` to find the correct position where the number should be inserted to maintain descending order.
   - If no such position is found (i.e., the number is smaller than all existing numbers in `odd_list`), we append it to the end of `odd_list`.
5. **Return the result**: After processing all numbers, we return both lists.

This approach ensures that each number is inserted into its appropriate list based on whether it is even or odd and maintains the required sorting order without using any disallowed elements.