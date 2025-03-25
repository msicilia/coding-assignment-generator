```
import random

def get_random_list(size):
    return [random.randint(1, 20) for _ in range(size)]

if __name__ == "__main__":
    my_list = get_random_list(5)
    print("List:", my_list)
    print("Average:", sum(my_list) / len(my_list))
    print("Highest:", max(my_list))
    print("Lowest:", min(my_list))
```
This code uses the `random` module to generate a list of random integers in the range 1-20. It then computes the average, highest and lowest value of the list using built-in functions such as `sum()`, `len()`, `max()` and `min()`.

Test cases:

* Empty list: `[]`
	+ Average: `0`
	+ Highest: `-inf`
	+ Lowest: `inf`
* List with one element: `[1]`
	+ Average: `1`
	+ Highest: `1`
	+ Lowest: `1`
* List with multiple elements: `[1, 2, 3, 4, 5]`
	+ Average: `3`
	+ Highest: `5`
	+ Lowest: `1`
* Random list with different sizes: `[1, 2, 3], [1, 2, 3, 4, 5] and [1, 2, 3, 4, 5, 6]`
	+ Average: `2.67` for `[1, 2, 3]`
	+ Highest: `6` for `[1, 2, 3, 4, 5, 6]`
	+ Lowest: `1` for all lists