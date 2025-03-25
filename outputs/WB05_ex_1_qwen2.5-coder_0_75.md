### Problem Description

We are given an original list of integers. We need to generate two lists:
1. One with even numbers sorted in ascending order.
2. Another with odd numbers sorted in descending order.

The generation of these lists must be done as we traverse the original list, inserting each number into the appropriate list based on whether it is even or odd.

### Constraints
- We cannot use match expressions or list comprehensions.
- We can only use lists or tuples for storing the results.

### Example Test Cases

1. Input: `[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]`
   - Expected Output:
     ```
     Even List: [2, 4, 6]
     Odd List: [9, 5, 5, 5, 3, 3, 1, 1]
     ```

2. Input: `[10, 22, 5, 75, 65, 80]`
   - Expected Output:
     ```
     Even List: [10, 22, 80]
     Odd List: [75, 65, 5]
     ```

3. Input: `[8, 4, 2, 10]`
   - Expected Output:
     ```
     Even List: [2, 4, 6, 8, 10]
     Odd List: []
     ```

4. Input: `[9, 7, 5, 3]`
   - Expected Output:
     ```
     Even List: []
     Odd List: [9, 7, 5, 3]
     ```

5. Input: `[0]`
   - Expected Output:
     ```
     Even List: [0]
     Odd List: []
     ```

### Python Code

```python
def generate_lists(original_list):
    even_list = []
    odd_list = []

    for num in original_list:
        if num % 2 == 0:
            # Insert into even_list maintaining ascending order
            i = 0
            while i < len(even_list) and even_list[i] < num:
                i += 1
            even_list.insert(i, num)
        else:
            # Insert into odd_list maintaining descending order
            i = 0
            while i < len(odd_list) and odd_list[i] > num:
                i += 1
            odd_list.insert(i, num)

    return even_list, odd_list

# Example test cases
print(generate_lists([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))
print(generate_lists([10, 22, 5, 75, 65, 80]))
print(generate_lists([8, 4, 2, 10]))
print(generate_lists([9, 7, 5, 3]))
print(generate_lists([0]))
```

### Explanation

1. **Initialization**: We initialize two empty lists, `even_list` and `odd_list`.

2. **Traversal**: We traverse each number in the original list.
   - If the number is even (`num % 2 == 0`), we insert it into the `even_list` while maintaining ascending order by finding the correct position using a simple linear search.
   - If the number is odd, we insert it into the `odd_list` while maintaining descending order.

3. **Output**: After processing all numbers, we return the two lists.

This code ensures that numbers are inserted in their respective lists sorted according to the specified criteria as they are traversed from the original list.