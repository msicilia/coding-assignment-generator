
To solve this problem, you can use a dictionary to store the pixels of the QR code and their corresponding colors (black or white). You can then use a loop to randomly generate the pixels of the QR code and store them in the dictionary. Finally, you can use another loop to display the QR code on the screen using asterisks.

Here is an example implementation:
```python
import random

# Define the dimensions of the QR code
version = 1
N = version * version

# Initialize the dictionary to store the pixels and their colors
pixels = {}
for i in range(N):
    for j in range(N):
        pixels[(i, j)] = random.choice(['black', 'white'])

# Display the QR code on the screen using asterisks
asterisk_string = ''
for i in range(N):
    for j in range(N):
        if pixels[(i, j)] == 'black':
            asterisk_string += '*'
        else:
            asterisk_string += ' '
    asterisk_string += '\n'
print(asterisk_string)
```
This code will randomly generate version 1 QR codes and display them on the screen using asterisks. Note that you can modify the `version` variable to generate different sizes of QR codes (version 2, version 3, etc.).