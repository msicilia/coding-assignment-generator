```
n = int(input("Enter a positive integer: "))

powers_of_two = []
powers_of_three = []
powers_of_five = []

for i in range(n):
    powers_of_two.append(2**i)
    powers_of_three.append(3**i)
    powers_of_five.append(5**i)

print("The n first powers of 2, 3 and 5 are:")
print("Two:", powers_of_two)
print("Three:", powers_of_three)
print("Five:", powers_of_five)
```