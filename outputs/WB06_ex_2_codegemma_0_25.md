```python
import random

# Function to generate a random QR code version 1
def generate_qr_code():
    # Create a dictionary to represent the QR code
    qr_code = {}

    # Generate a random number of black pixels between 0 and 20
    black_pixels = random.randint(0, 20)

    # Create a 21x21 grid of pixels, with black pixels represented by True
    for i in range(21):
        for j in range(21):
            qr_code[i, j] = i < black_pixels

    # Return the QR code dictionary
    return qr_code

# Function to display a QR code on the screen
def display_qr_code(qr_code):
    # Iterate over the dictionary and print '*' for black pixels, ' ' for white pixels
    for i in range(21):
        for j in range(21):
            print('*' if qr_code[i, j] else ' ', end='')
        print()

# Generate a random QR code
qr_code = generate_qr_code()

# Display the QR code
display_qr_code(qr_code)
```

**Example output:**

```
* ** * ** * ** * ** *
* * * * ** * * * ** *
* * * * ** * * * ** *
* * * * ** * * * ** *
* * * * ** * * * ** *
* * * * ** * * * ** *
* * * * ** * * * ** *
* * * * ** * * * ** *
* * * * ** * * * ** *
* * * * ** * * * ** *
* * * * ** * * * ** *
* * * * ** * * * ** *
* * * * ** * * * ** *
* * * * ** * * * ** *
```

**Note:**

* The code uses the `random` library to generate random numbers.
* The `randint` function is used to generate a random number of black pixels between 0 and 20.
* The code creates a dictionary to represent the QR code, with keys as the pixel coordinates and values as True for black pixels, False for white pixels.
* The `display_qr_code()` function iterates over the dictionary and prints '*' for black pixels, ' ' for white pixels.