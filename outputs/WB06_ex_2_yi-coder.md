Here's how you can program such an application in Python:

```python
import random 

def generate_qr():
    code = {} # Initialize empty dictionary for QR code
    for i in range(21): # Loop for each row (QR version 1 is a 21x21 matrix)
        row = [] # Empty list for each row
        for j in range(21): # Another loop to create each row with random white or black pixels
            pixel = random.randint(0,1) # Generate random pixel (0=white, 1=black)
            if pixel == 0:
                row.append(' ')  # Add white space for "white" pixels
            else:
                row.append('*')  # Add an asterisk for "black" pixels
        code[i] = row # Add the row to the dictionary representation of QR code
    return code 

def print_qr(code):
    for i in range(21): # Loop over each key-value pair (row) in the QR code
        print(''.join(code[i]))  # Join all characters together into a single string for printing

qr = generate_qr()   # Generate and print a random version 1 QR code
print_qr(qr)```