Here's how you can solve it:
```python
import random  # Python module for generating random numbers

def list_operations(n):
    """Generate a list of n random integers in the range 1..20, compute their average, min and max values"""
    list_of_integers = []  # create an empty list

    for _ in range(n):  # loop 'n' times
        # append a random integer to the list (between 1 and 20 inclusive)
        list_of_integers.append(random.randint(1, 20))

    return sum(list_of_integers)/len(list_of_integers), min(list_of_integers), max(list_of_integers)  # return average, min and max of the list values

print("Average: {}, Min: {}, Max: {}".format(*list_operations(10)))  # generate a list of 10 random numbers and print their average, min and max
```
This Python code defines a function `list_operations` that generates a certain number (specified by the user) of random integers in the range [1,20]. It then computes and returns three values: the average value of these integers, the minimum integer found in the list and the maximum integer found in the list. The `random` module's randint function provides a random number within the specified range, and these random values are added into the list using a for loop structure. Finally, the function returns the computed average, minimum and maximum integer value from the generated list of numbers. This return value is then printed out in the format 'Average: value, Min: value, Max: value' after being deconstructed by the `*` operator within the `print()` function call.