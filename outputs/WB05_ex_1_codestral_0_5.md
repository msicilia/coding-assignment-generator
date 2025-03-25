 Thoughts: To solve this problem, I will create two empty lists to store the even and odd numbers. Then, I will iterate over the original list of integers. For each number, I will check if it is even or odd. If it is even, I will insert it into the even list at the correct sorted position. If it is odd, I will insert it into the odd list at the correct sorted position.

   Code:
```py
def separate_lists(original):
    even_list = []
    odd_list = []

    for num in original:
        if num % 2 == 0:
            # insert number into even_list at the correct sorted position
            i = 0
            while i < len(even_list) and even_list[i] < num:
                i += 1
            even_list.insert(i, num)
        else:
            # insert number into odd_list at the correct sorted position
            i = 0
            while i < len(odd_list) and odd_list[i] > num:
                i += 1
            odd_list.insert(i, num)

    return even_list, odd_list
```
I have defined a function `separate_lists` that takes an original list of integers as input and returns two lists: one with the even numbers sorted in ascending order and another with the odd numbers sorted in descending order. The function uses two empty lists, `even_list` and `odd_list`, to store the even and odd numbers respectively.

The function then iterates over each number in the original list. If the number is even, it is inserted into the `even_list` at the correct sorted position using a while loop. If the number is odd, it is inserted into the `odd_list` at the correct sorted position using another while loop.

Finally, the function returns the two lists as a tuple: `(even_list, odd_list)`.