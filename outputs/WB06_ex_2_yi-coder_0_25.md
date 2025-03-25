Here is an example of how you could program such a application in Python without using match expressions or list comprehensions:

```python
import random 
  
def generate_qr_code():
    # Define the size of the QR code. For version 1, it's a 21x21 matrix.
    size = 21
    # Create an empty string to represent the QR code.
    qr_code = ''
    for _ in range(size):
        line = ''
        for _ in range(size):
            # Add either a white or black pixel represented by a space or an asterisk into the line.
            pixel = '*' if random.randint(0, 1) else ' '
            line += pixel
        # Add a new line character to the end of each line except for the last line.
        qr_code += line + '\n'
    return qr_code
  
print(generate_qr_code())
```
This Python program creates an application that generates version 1 QR codes represented by an NxN square with pixels that can be white or black as described in the problem. The "random" library and "randint" function are used to generate the random numbers needed for determining if a pixel is white or black (0 = white, 1 = black).