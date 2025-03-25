Certainly! Below is the Python code to randomly generate version 1 QR codes (21x21 pixels) and display them on the screen using asterisks. The code uses dictionaries as required and does not include match expressions or list comprehensions.

```python
import random

def generate_qr_code():
    # Create an empty dictionary to store the QR code pixels
    qr_code = {}
    
    # Iterate over each row in the 21x21 grid
    for y in range(21):
        # Iterate over each column in the 21x21 grid
        for x in range(21):
            # Generate a random pixel value (0 for white, 1 for black)
            pixel_value = random.randint(0, 1)
            
            # Store the pixel value in the dictionary with coordinates as keys
            qr_code[(x, y)] = '*' if pixel_value == 1 else ' '

    return qr_code

def display_qr_code(qr_code):
    # Iterate over each row in the 21x21 grid
    for y in range(21):
        # Retrieve and print each row of pixels as a string
        row = ''.join(qr_code[(x, y)] for x in range(21))
        print(row)

# Generate a random QR code
qr_code = generate_qr_code()

# Display the generated QR code
display_qr_code(qr_code)
```

### Explanation:

1. **generate_qr_code() Function:**
    - A dictionary `qr_code` is created to store the pixel values.
    - Nested loops iterate over each cell in a 21x21 grid (from `(0, 0)` to `(20, 20)`).
    - For each cell, a random integer between 0 and 1 is generated using `random.randint(0, 1)`.
    - If the random number is 1, it is stored as an asterisk (`'*'`), representing a black pixel. Otherwise, a space (`' '`), representing a white pixel, is stored.
    - The dictionary key is a tuple `(x, y)` representing the coordinates of each cell.

2. **display_qr_code() Function:**
    - Iterates over each row in the 21x21 grid (from `0` to `20`).
    - For each row, it constructs a string by joining the pixel values for that row using `''.join(...)`.
    - Prints the constructed row.

This code will generate and display a random version 1 QR code consisting of asterisks representing black pixels and spaces representing white pixels.