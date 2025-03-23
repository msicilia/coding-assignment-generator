 Thought: I will define a recursive function named `find_number` which takes two arguments - a target number and a list of numbers. The function will check if the first element of the list is equal to the target number. If it is, the function will return True. If not, the function will call itself with the target number and the rest of the list (excluding the first element). The function will continue this process until it has checked all elements in the list or found the target number.

   Code:
   ```python
   def find_number(num, lst):
       if len(lst) == 0:
           return False
       elif num == lst[0]:
           return True
       else:
           return find_number(num, lst[1:])

   # test cases
   print(find_number(5, [1, 2, 3, 4, 5])) # expected output: True
   print(find_number(6, [1, 2, 3, 4, 5])) # expected output: False
   ```