Here is an example code for the problem:
```python
def recursive_multiply(num1, num2):
    # Base case if one of the numbers is zero then return 0
    if num1 == 0 or num2 == 0:
        return 0

    # If num1 is less than num2 swap the numbers. This is to reduce the number of recursive calls made.
    if num1 < num2:
        num1, num2 = num2, num1

    # Recursively add num1 to result. The number of times it is added is given by (num2-1)
    return num1 + recursive_multiply(num1, num2 - 1)

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print(f'The product is {recursive_multiply(num1, num2)}')

if __name__ == "__main__":
    main()
```