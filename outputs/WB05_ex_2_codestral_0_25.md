 ```python
   import random

   # create an empty list
   numbers = []

   # generate and append 10 random numbers to the list in the range 1..20
   for _ in range(10):
       numbers.append(random.randint(1, 20))

   # calculate the sum of all elements in the list
   total = 0
   for number in numbers:
       total += number

   # compute the average by dividing the total by the length of the list
   average = total / len(numbers)

   # find the highest value using the max() function
   max_value = max(numbers)

   # find the lowest value using the min() function
   min_value = min(numbers)

   # print all results
   print('Average:', average)
   print('Maximum value:', max_value)
   print('Minimum value:', min_value)
   ```