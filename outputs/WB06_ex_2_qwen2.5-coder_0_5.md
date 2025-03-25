Sure! Below is an example of Python code that generates a version 1 (21x21) QR code randomly and displays it using asterisks:

```python
import random

def generate_qr_code(version):
    n = version * 4 + 17  # Calculate the size of the QR code based on the version
    qr_code = {}

    for i in range(n):
        for j in range(n):
            if (i < 8 and j < 8) or (i >= n - 8 and j >= n - 8) or \
               (i == 8 and j >= 7 and j <= n - 9) or (j == 8 and i >= 7 and i <= n - 9):
                qr_code[(i, j)] = ' '
            else:
                if random.randint(0, 1) == 0:
                    qr_code[(i, j)] = '*'
                else:
                    qr_code[(i, j)] = ' '

    return qr_code

def display_qr_code(qr_code):
    n = len(list(qr_code.keys()))
    
    for i in range(n):
        for j in range(n):
            print(qr_code.get((i, j), ' '), end='')
        print()

# Generate and display a version 1 QR code
qr_code = generate_qr_code(1)
display_qr_code(qr_code)
```

### Explanation:
1. **Function `generate_qr_code(version)`**:
   - This function takes the version number (in this case, it's always version 1) and calculates the size of the QR code.
   - It then iterates through each pixel in the QR code grid. For certain positions (corners, finder patterns), it sets the pixel to a space (' '). For other pixels, it randomly assigns either an asterisk ('*') or a space (' ') using `random.randint(0, 1)`.

2. **Function `display_qr_code(qr_code)`**:
   - This function takes the generated QR code dictionary and displays it on the screen.
   - It iterates through each pixel in the grid and prints the corresponding character (either '*' or ' ') from the dictionary.

### Example Test Case:

Running the above code will generate a random version 1 QR code and display it using asterisks. Since the generation is random, different runs will produce different QR codes.

You can use this code as part of your Python course to teach students how to use dictionaries and the `random` library to generate and display QR codes randomly.