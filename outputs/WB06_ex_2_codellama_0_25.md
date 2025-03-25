[PYTHON]
import random

def generate_qr_code(size):
    if size == 1:
        version = 1
    else:
        version = random.randint(1, 40)
    code = {}
    for i in range(version ** 2):
        code[i] = random.choice([0, 1])
    return code

def display_qr_code(code):
    version = int(len(code) ** 0.5)
    for i in range(version ** 2):
        if code[i] == 0:
            print(" ", end="")
        else:
            print("*", end="")
        if i % version == version - 1:
            print()
[/PYTHON]
[TESTS]
# Test case 1:
assert generate_qr_code(2) == {'0,0': 0, '0,1': 0, '1,0': 0, '1,1': 0}

# Test case 2:
assert generate_qr_code(3) == {'0,0': 0, '0,1': 0, '0,2': 0, '1,0': 0, '1,1': 0, '1,2': 0, '2,0': 0, '2,1': 0, '2,2': 0}

# Test case 3:
assert generate_qr_code(4) == {'0,0': 0, '0,1': 0, '0,2': 0, '0,3': 0, '1,0': 0, '1,1': 0, '1,2': 0, '1,3': 0, '2,0': 0, '2,1': 0, '2,2': 0, '2,3': 0, '3,0': 0, '3,1': 0, '3,2': 0, '3,3': 0}

# Test case 4:
assert generate_qr_code(5) == {'0,0': 0, '0,1': 0, '0,2': 0, '0,3': 0, '0,4': 0, '1,0': 0, '1,1': 0, '1,2': 0, '1,3': 0, '1,4': 0, '2,0': 0, '2,1': 0, '2,2': 0, '2,3': 0, '2,4': 0, '3,0': 0, '3,1': 0, '3,2': 0, '3,3': 0, '3,4': 0, '4,0': 0, '4,1': 0, '4,2': 0, '4,3': 0, '4,4': 0}
[/TESTS]
