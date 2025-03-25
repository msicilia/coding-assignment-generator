
To solve this problem, you can use dictionaries to store the pixels of the QR code. You can then use a loop to randomly generate the pixels and display them on the screen using asterisks.

Here is an example of how you can do this:
```python
import random

# Define the size of the QR code (version 1)
size = 21

# Initialize an empty dictionary to store the pixels
pixels = {}

# Loop through each pixel and randomly generate its value (white or black)
for i in range(size):
    for j in range(size):
        # Use the random library to generate a random number between 0 and 1
        rand_num = random.random()
        
        # If the random number is less than 0.5, set the pixel value to white (1), otherwise set it to black (0)
        if rand_num < 0.5:
            pixels[(i, j)] = 1
        else:
            pixels[(i, j)] = 0

# Display the QR code on the screen using asterisks
for i in range(size):
    for j in range(size):
        # If the pixel value is white (1), display an asterisk (*) on the screen
        if pixels[(i, j)] == 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
```
This code will generate a QR code of size 21x21 and display it on the screen using asterisks. You can modify the value of the `size` variable to change the size of the QR code that is generated.