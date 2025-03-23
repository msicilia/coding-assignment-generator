 Code:
   ```py
   import random

   # Initialize an empty list
   numbers = []

   # Generate 10 random integers between 1 and 20 and add them to the list
   for _ in range(10):
       num = random.randint(1, 20)
       numbers.append(num)

   print("List of numbers:", numbers)

   # Initialize variables for average calculation and min/max values
   total = 0
   min_val = float('inf')
   max_val = float('-inf')

   # Calculate the sum of all elements in the list and find the min/max values
   for num in numbers:
       total += num
       if num < min_val:
           min_val = num
       if num > max_val:
           max_val = num

   # Calculate the average
   avg = total / len(numbers)

   print("Average of numbers:", avg)
   print("Minimum value in list:", min_val)
   print("Maximum value in list:", max_val)
   ```