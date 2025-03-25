```python
def multiply(n1, n2):
    # Base case when one or both inputs are 0
    if n1 == 0 or n2 == 0:
        return 0
    elif n2 < 0:  # If second number is negative, invert the result
        return -multiply(n1, -n2)
    else:
        # Recursive case when second input > 0
        return (n1 + multiply(n1, n2 - 1))

def get_number(prompt):
    while True:  # Keep asking until valid number entered
        try:
            num = int(input(prompt))
            break
        except ValueError:
            print('Invalid input! Please enter a whole number.')
    return num

def main():
    n1 = get_number('Enter the first number to multiply (it can be negative): ')
    n2 = get_number('Enter the second number to multiply (it should not be 0): ')
    print(f'The result of multiplication is: {multiply(n1, n2)}')

main()
```