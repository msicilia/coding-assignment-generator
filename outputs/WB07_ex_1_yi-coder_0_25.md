Here's how one can write such a program in Python using recursive function calls and without using the multiplication operator.
```python
def multiply(x, y):
    if x == 0 or y == 0:  # base case for our recursion
        return 0
    elif x > 0:  # when x is positive we add y to itself 'x' times recursively
        return (y + multiply(x-1, y))
    else: # if x is negative, we reverse the sign of both x and y and do the same process above
        return -multiply(-x, -y)

def get_input():
    print("Enter first number:")
    a = int(input())
    print("Enter second number:")
    b = int(input())
    return a, b

def main():
    x, y = get_input()  # getting the two numbers to be multiplied from user input
    result = multiply(x, y) # multiplying x and y recursively 
    print("The product of {} and {} is: {}".format(x, y, result))

if __name__ == "__main__":
    main()  # calling main function to execute our program
```