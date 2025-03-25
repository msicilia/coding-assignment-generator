 Thoughts:
   To solve this problem, we will use a dictionary to map the binary values (0 and 1) to their corresponding pixel values (' ' for white and '*' for black). We will then iterate through the rows and columns of the QR code, generating random numbers between 0 and 1 to represent the pixel value. We can then append the corresponding pixel value to a string that represents the row. Once we have generated all the pixels for a row, we can add the row to our QR code list. Finally, we will print each row of the QR code to display it on the screen.

   Code:
   ```python
import random
# Define a dictionary to map 0 and 1 to ' ' and '*' respectively
pixel_dict = {0: ' ', 1: '*'}
# Initialize an empty list to store the QR code
qr_code = []
# Generate a 21x21 pixel QR code
for i in range(21):
    row = ''
    for j in range(21):
        # Generate a random number between 0 and 1
        num = random.randint(0, 1)
        # Map the number to its corresponding pixel value
        pixel = pixel_dict[num]
        # Add the pixel to the current row
        row += pixel
    # Add the current row to the QR code
    qr_code.append(row)
# Print the QR code
for row in qr_code:
    print(row)
   ```