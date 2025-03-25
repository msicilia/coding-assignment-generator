 Code:
```python
def int_to_roman(num):
    symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    result = ''
    i = 0
    while num > 0:
        if num >= values[i]:
            num -= values[i]
            result += symbols[i]
        else:
            i += 1
    return result
# Test cases
print(int_to_roman(45))    # Output: XLV
print(int_to_roman(900))   # Output: CM
print(int_to_roman(2000))  # Output: MM
```
The code defines a function `int_to_roman` that takes an integer as input and returns its Roman numeral representation. The function uses two lists: `symbols`, which contains the Roman symbols, and `values`, which contains their corresponding values. In a loop, the function finds the largest value less than or equal to the input number, subtracts it from the input number, and appends its corresponding symbol to the result string. The loop continues as long as the input number is greater than 0. Finally, the function returns the result string.

The test cases demonstrate that the function correctly converts the Arabic numerals 45, 900, and 2000 to their Roman numeral representations XLV, CM, and MM, respectively.