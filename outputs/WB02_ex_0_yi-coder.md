Here is Python code which meets all your requirements:

```python
def force(mass, acceleration):
    return mass * acceleration

def tester():
    #Test Case 1
    assert force(10,2) == 20, "Test case 1 Failed" # Mass = 10kg and Acceleration = 2m/s^2.
    print("Force for test case 1 is: ",force(10,2))
    #Test Case 2
    assert force(50,3) == 150, "Test case 2 Failed" # Mass = 50kg and Acceleration = 3m/s^2.
    print("Force for test case 2 is: ",force(50,3))
    #Test Case 3
    assert force(75,4) == 300, "Test case 3 Failed" # Mass = 75kg and Acceleration = 4m/s^2.
    print("Force for test case 3 is: ",force(75,4))

tester()
```
This code first implements the `force` function that calculates force from given mass and acceleration values using the formula F=ma. Then it defines a tester function where several test cases are defined to validate this functionality. Each test case validates the expected output against the actual output for specific inputs, and finally all these tests are executed by calling the `tester` function.
The use of assert statements in the `tester()` function allows us to execute our test cases, which will check whether the force function is working as expected or not. If there's an error, it prints a failure message along with the failed test case details and stops execution. Otherwise, it simply prints the calculated force for that test case and proceeds to the next one till completion.