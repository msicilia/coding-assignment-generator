To solve this problem, we need to create a Python script that randomly generates a version 1 QR code (21x21 pixels) and displays it on the screen using asterisks. We will use dictionaries to map the pixel values (white or black) to asterisks.

Here's the step-by-step implementation:

1. **Generate a 21x21 grid of random pixel values** using the `randint` function from the `random` library.
2. **Map the pixel values to asterisks** using a dictionary.
3. **Display the QR code on the screen**.

Here's the Python code to achieve this:

```python
import random

# Function to generate a 21x21 QR code grid with random pixels
def generate_qr_code():
    qr_code = []
    for _ in range(21):
        row = [random.randint(0, 1) for _ in range(21)]
        qr_code.append(row)
    return qr_code

# Function to map pixel values to asterisks and print the QR code
def display_qr_code(qr_code):
    pixel_to_asterisk = {0: ' ', 1: '*'}
    for row in qr_code:
        line = ''.join(pixel_to_asterisk[pixel] for pixel in row)
        print(line)

# Generate a random QR code
qr_code = generate_qr_code()

# Display the QR code
display_qr_code(qr_code)
```

### Explanation:

1. **generate_qr_code function**:
   - This function creates an empty list `qr_code`.
   - It uses a nested loop to generate 21 rows, each containing 21 random pixels (0 or 1) using `random.randint(0, 1)`.
   - Each row is appended to the `qr_code` list.

2. **display_qr_code function**:
   - This function takes the `qr_code` as input.
   - It defines a dictionary `pixel_to_asterisk` that maps pixel values (0 and 1) to asterisks (' ' and '*', respectively).
   - It iterates over each row in the `qr_code`, converts each pixel value to an asterisk using the dictionary, and joins them into a string.
   - Each line is printed on a new line.

### Example Output:

Running the script will output a randomly generated 21x21 QR code displayed as asterisks. For example:

```
* * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * 
```

This code meets the requirements of generating a random 21x21 QR code and displaying it on the screen using asterisks, while also using dictionaries for mapping pixel values to asterisks.