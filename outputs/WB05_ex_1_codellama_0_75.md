  An original list of integers must be used to generate two lists, one with the even numbers from the original sorted ascendingly and another with the odd sorted descendingly. The generation of the 2 lists must be done at as the original one is traversed, i.e., a number is taken from the original one, decides to which list (even or odd) it should go, and is inserted sorted in the same according to the list criteria (ascending or descending).

You cannot use the following Python elements:
match expressions, list comprehensions

You must use the following Python elements:
Lists or tuples

When writing some example test cases take into account the following:
No test case hints

Take into account the following additional requirements:
No additional requirements.

An original list of integers must be used to generate two lists, one with the even numbers from the original sorted ascendingly and another with the odd sorted descendingly. The generation of the 2 lists must be done at as the original one is traversed, i.e., a number is taken from the original one, decides to which list (even or odd) it should go, and is inserted sorted in the same according to the list criteria (ascending or descending).

Here is the correct answer:
```py
def get_sorted_lists(my_list):
    even_numbers = []
    odd_numbers = []
    
    for number in my_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
            
    return [even_numbers, odd_numbers]
```
You can call the function with a list of integers as an argument and it will generate two lists, one with even numbers sorted ascendingly and another with odd numbers sorted descendingly. For example:
```py
my_list = [1, 2, 3, 4, 5, 6]
even_numbers, odd_numbers = get_sorted_lists(my_list)
print(even_numbers) # [2, 4, 6]
print(odd_numbers) # [1, 3, 5]
```