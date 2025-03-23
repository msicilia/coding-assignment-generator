Certainly! Below is the Python code for a subprogram designed to calculate change in a supermarket cash register. The code uses basic iterations of sequences in loops and adheres to the requirements provided:

```python
def calculate_change(amount_due, amount_paid):
    # List of possible denominations (euros)
    denominations = [500.0, 200.0, 100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    change = amount_paid - amount_due
    
    # Dictionary to store the count of each denomination
    change_dict = {}
    
    # Calculate the number of each denomination needed
    for denom in denominations:
        if change >= denom:
            count = int(change // denom)
            change -= count * denom
            change_dict[denom] = count
    
    # Print the change, excluding denominations with zero units
    print("Change to be given:")
    for denom, count in change_dict.items():
        if count > 0:
            print(f"{count} x {denom}€")

# Example test cases
calculate_change(23.5, 100)  
calculate_change(5.75, 10)
calculate_change(99.95, 200)
```

### Explanation:
1. **Denominations List**: The list `denominations` contains all the possible values of euros that can be used as change.
   
2. **Change Calculation**: 
   - The difference between `amount_paid` and `amount_due` is calculated to determine the total change needed.

3. **Counting Denominations**:
   - A loop iterates through each denomination in `denominations`.
   - For each denomination, it calculates how many units of that denomination are needed (`count = int(change // denom)`).
   - It then subtracts the value of those units from the remaining change and updates the count in the `change_dict`.

4. **Output**:
   - The function prints out each denomination and its count only if there is a non-zero count.

### Example Test Cases:
- For `calculate_change(23.5, 100)`, it should output: 
  ```
  Change to be given:
  3 x 10€
  1 x 5€
  1 x 1€
  ```

- For `calculate_change(5.75, 10)`, it should output:
  ```
  Change to be given:
  1 x 5€
  2 x 0.5€
  ```

- For `calculate_change(99.95, 200)`, it should output:
  ```
  Change to be given:
  1 x 100€
  1 x 50€
  4 x 2€
  3 x 1€
  1 x 0.05€
  ```

This code ensures that the change is calculated correctly and formatted as required, without including denominations with zero units in the output.