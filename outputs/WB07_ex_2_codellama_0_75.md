  Write Python code to solve the problem:
Perform a recursive function that given an integer, counts its number of digits.
You cannot use the following Python elements:
match expressions, list comprehensions
You must use the following Python elements:
Recursive function calls.
Write a function that takes an integer as input and returns the number of digits in that integer. The function should be recursive, meaning it should call itself to solve the problem.

def count_digits(n):
    if n < 0:
        return -1
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

You are a Python instructor in an introduction to programming course at graduate level.
Write Python code to solve the problem:
Perform a recursive function that given an integer, counts its number of digits.
You cannot use the following Python elements:
match expressions, list comprehensions
You must use the following Python elements:
Recursive function calls.
When writing some example test cases take into account the following:
No test case hints
Take into account the following additional requirements:
No additional requirements.