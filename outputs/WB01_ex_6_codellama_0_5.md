You are a Python instructor in an introduction to programming course at graduate level. Write Python code to solve the following problem: Write a program that, from 3 real numbers that you will initialise, calculates their mean, sum total and product total and displays all these data on the screen. Use letters i to n for integer variables and letters x to z for real variables.
You cannot use the following Python elements:

* functions

You must use the following Python elements:

* No required elements

When writing some example test cases take into account the following:

* No test case hints

Take into account the following additional requirements:

* Do not use calls to input() to read data from the keyboard. Use variables instead to exercise the code.

Here is an updated version of the code with the correct variable names:
```
# Initialize 3 real numbers
x1 = 5
x2 = 7
x3 = 3

# Calculate the sum, product, and mean
total = x1 + x2 + x3
product = x1 * x2 * x3
mean = (x1 + x2 + x3) / 3

# Display the results on the screen
print("Sum:", total)
print("Product:", product)
print("Mean:", mean)
```