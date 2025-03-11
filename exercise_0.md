```python
def sum_of_elements(lst):
    """
    Returns the sum of all elements in a given list of integers.
    
    Args:
    lst (list): A list of integers.
    
    Returns:
    int: The sum of all elements in the list.
    """
    total = 0  # Initialize the total to zero
    for element in lst:  # Iterate through each element in the list
        total += element  # Add the current element to the total
    return total  # Return the total sum

# Example test cases
print(sum_of_elements([1, 2, 3]))  # Expected output: 6
print(sum_of_elements([-1, -2, -3]))  # Expected output: -6
print(sum_of_elements([0, 0, 0]))  # Expected output: 0
print(sum_of_elements([]))  # Expected output: 0
```