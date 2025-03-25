Here is an example of how you can solve this problem:
```python
import random 

def create_qr():
    # Define size of QR code
    size = 21

    # Create a blank string for the qr representation
    qr_code = ''

    for _ in range(size):
        row = ''
        for _ in range(size):
            pixel = random.randint(0, 1)
            if pixel == 1:
                row += '*'  # Black pixel represented by an asterisk
            else:
                row += ' '  # White pixel represented by a space
        qr_code += row + '\n'  # Add newline character at the end of each line
    return qr_code

def display_qr(Qr):
    print(Qr)

QR = create_qr()
display_qr(QR)
```
The above python program uses a nested loop to generate an NxN square (in this case 21x21 for version 1 QR code). For each pixel, it randomly generates a number between 0 and 1 using random.randint(0, 1). If the generated number is 1, then it's a black pixel represented by an asterisk; if not, it's a white pixel represented by a space.