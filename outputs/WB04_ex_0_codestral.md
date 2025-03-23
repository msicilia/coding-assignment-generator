 I have corrected the code based on your feedback and provided a revised solution below. The revised code fixes the incorrect representation of 40 as "XXXL" and changes it to "XL". Now the function correctly converts an Arabic numeral year to Roman numerals within the range 1 to 2000.

```python
def arabic_to_roman(arabic):
    if not (1 <= arabic <= 2000):
        return "Invalid input"

    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    result = ""
    for value, numeral in roman_numerals.items():
        while arabic >= value:
            result += numeral
            arabic -= value

    return result
```

You can test the function with various Arabic numeral years as follows:

```python
print(arabic_to_roman(1984))  # Output: MCMLXXXIV
print(arabic_to_roman(2000))  # Output: MM
print(arabic_to_roman(57))    # Output: LVII
```