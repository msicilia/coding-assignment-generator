Certainly! Below is the Python code for the function `calculate_average` that meets the specified requirements:

```python
def calculate_average(numbers):
    """
    Calculate the average of all elements in a list of integers.
    
    Parameters:
        numbers (list): A list of integers.
        
    Returns:
        float: The average of the elements in the list. If the list is empty, returns None.
        
    Raises:
        ValueError: If the input is not a list or if the list contains non-integer elements.
    """
    
    # Check if the input is a list
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list.")
    
    # Check if the list contains only integers
    for num in numbers:
        if not isinstance(num, int):
            raise ValueError("List must contain only integer elements.")
    
    # Calculate the sum of the list
    total_sum = 0
    for num in numbers:
        total_sum += num
    
    # Calculate the average
    count = len(numbers)
    if count == 0:
        return None
    
    average = total_sum / count
    return average

# Example test cases
def run_tests():
    """
    Run example test cases to validate the `calculate_average` function.
    """
    
    # Test case with positive numbers
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0, "Test case 1 failed"
    
    # Test case with negative numbers
    assert calculate_average([-10, 0, 10]) == 0.0, "Test case 2 failed"
    
    # Test case with mixed positive and negative numbers
    assert calculate_average([10, -5, 3, 7]) == 6.0, "Test case 3 failed"
    
    # Test case with a single element
    assert calculate_average([42]) == 42.0, "Test case 4 failed"
    
    # Test case with an empty list
    assert calculate_average([]) is None, "Test case 5 failed"
    
    print("All test cases passed.")

# Run the tests
run_tests()
```

### Explanation:

1. **Function Definition and Docstring**:
   - The function `calculate_average` takes a single parameter `numbers`, which should be a list of integers.
   - A docstring is provided to describe the purpose, parameters, return value, and possible exceptions.

2. **Input Validation**:
   - The function first checks if the input is a list using `isinstance(numbers, list)`. If not, it raises a `ValueError`.
   - It then iterates through each element in the list to ensure all elements are integers using `isinstance(num, int)`. If any non-integer is found, it raises a `ValueError`.

3. **Sum Calculation**:
   - The function calculates the sum of the list using a for loop.

4. **Average Calculation**:
   - It checks if the count of elements in the list is zero to avoid division by zero. If not, it calculates the average and returns it.

5. **Test Cases**:
   - A `run_tests` function is provided to run example test cases that cover various scenarios (positive numbers, negative numbers, mixed numbers, single element, empty list).

This code should meet all the specified requirements and provide a robust implementation of the average calculation function.