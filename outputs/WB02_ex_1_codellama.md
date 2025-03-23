Sure! Here's an answer to the user task:

You are a Python instructor in an introduction to programming course at graduate level.
 
Write Python code to solve the following problem:
The Barn is a unit of surface area widely used in particle physics, which is equivalent to 10-28 m². To illustrate its size, note that a Barn is approximately the cross-sectional area of the nucleus of a uranium atom. Program two functions, one allowing to convert units in m² to Barns, and its inverse

You cannot use the following Python elements:
Data structures in general. The solutions should deal with variables of basic data types., Loops, Conditional statements

You must use the following Python elements:
functions

When writing some example test cases take into account the following:
No test case hints

Take into account the following additional requirements:
The results of the coding has to follow the good practices of modularity, including information hiding, and the use of functions.

 The Barn is a unit of surface area widely used in particle physics, which is equivalent to 10-28 m². To illustrate its size, note that a Barn is approximately the cross-sectional area of the nucleus of a uranium atom. Program two functions, one allowing to convert units in m² to Barns, and its inverse

Here is an example of how you could approach this task:
```
def convert_m2_to_barn(area):
    return area * 10**-28

def convert_barn_to_m2(area):
    return area / 10**-28

# Test cases
assert convert_m2_to_barn(100) == 10**-28
assert convert_barn_to_m2(10**-28) == 100
```
In this code, we define two functions: `convert_m2_to_barn` and `convert_barn_to_m2`. These functions take a single argument `area`, which represents the area in square meters (m²), and return the equivalent value in barns.

The first function, `convert_m2_to_barn`, simply returns the input area multiplied by 10 to the power of -28, since there are 10 barns per square meter.

The second function, `convert_barn_to_m2`, returns the input area divided by 10 to the power of -28, since there are 10^28 square meters in a barn.

To test the functions, we define two test cases that assert the correctness of the conversions. The first test case asserts that converting 100 m² to barns gives us 10^(-28), and the second test case asserts that converting 10^(-28) barns back to m² gives us 100.

Note that we are using the `assert` statement to write these tests, which allows us to write simple unit tests without having to set up a separate testing framework.