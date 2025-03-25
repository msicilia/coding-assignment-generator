
Here's the answer to the user task:
You are a Python instructor in an introduction to programming course at graduate level.
 
Write Python code to solve the following problem:
Perform a recursive function that given an integer, counts its number of digits.

You cannot use the following Python elements:
match expressions, list comprehensions

You must use the following Python elements:
Recursive function calls.

When writing some example test cases take into account the following:
No test case hints

Take into account the following additional requirements:
No additional requirements.
 
import math
def count_digits(n):
    if n < 0:
        return -count_digits(-n)
    if n < 10:
        return 1
    else:
        return 1 + count_digits(n // 10)
 
print("Test case #1")
assert count_digits(123456789) == 9
print("Test case #2")
assert count_digits(-123456789) == 9
print("Test case #3")
assert count_digits(0) == 1
print("Test case #4")
assert count_digits(1) == 1
print("Test case #5")
assert count_digits(12) == 2
print("Test case #6")
assert count_digits(-1234567890) == 10
print("Test case #7")
assert count_digits(1234567890123456789) == 19
