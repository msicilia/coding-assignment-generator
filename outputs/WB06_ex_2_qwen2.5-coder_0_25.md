Certainly! Below is the Python code that meets all the requirements specified:

```python
import random

def generate_qr_code(version):
    # Define the size of the QR code based on version
    if version != 1:
        raise ValueError("This implementation only supports version 1 QR codes.")
    
    n = 21  # Size of the QR code for version 1
    qr_code = {}

    # Generate random pixels
    for i in range(n):
        for j in range(n):
            qr_code[(i, j)] = random.randint(0, 1)

    return qr_code

def display_qr_code(qr_code):
    n = len(qr_code)
    
    for i in range(n):
        row = ""
        for j in range(n):
            if qr_code[(i, j)] == 0:
                row += " "
            else:
                row += "*"
        print(row)

# Generate and display a random version 1 QR code
qr_code = generate_qr_code(1)
display_qr_code(qr_code)
```

### Explanation:

1. **generate_qr_code(version)**: This function generates a random QR code for version 1. It uses the `random.randint` function to create a dictionary where each key-value pair represents a pixel in the QR code grid.

2. **display_qr_code(qr_code)**: This function takes a QR code (dictionary) and displays it on the screen using asterisks (*) for black pixels and spaces for white pixels.

3. **Main Execution**: The script generates a random version 1 QR code and then displays it.

### Example Test Cases:

- Run the script multiple times to see different randomly generated QR codes.
- Note that the only valid version supported is version 1, so attempting to generate any other version will raise an error.

This implementation adheres to all the constraints provided in the problem statement, including the use of dictionaries and avoiding list comprehensions and match expressions.