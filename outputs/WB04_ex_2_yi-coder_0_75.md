Here is how you can solve this problem using Python:
```python
n = int(input('Enter a positive number (n): '))  # read input from user

if n <= 0:
    print('Number must be positive')
else:
    powers_of_2 = [2 ** i for i in range(1, n+1)]   # generate powers of 2
    powers_of_3 = [3 ** i for i in range(1, n+1)]   # generate powers of 3
    powers_of_5 = [5 ** i for i in range(1, n+1)]   # generate powers of 5

    print('Powers Table:')
    for i in range(n):
        print(f'Power {i+1}: \t{powers_of_2[i]}\t\t{powers_of_3[i]}\t\t{powers_of_5[i]}')  # print powers of 2, 3 and 5
```