```python
def convert_to_roman(year):
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

    roman_year = []
    for numeral in sorted(roman_numerals.keys(), reverse=True):
        while year >= numeral:
            roman_year.append(roman_numerals[numeral])
            year -= numeral

    return ''.join(roman_year)

# Example usage:
year = int(input("Enter a year between 1 and 2000: "))
roman_year = convert_to_roman(year)
print(f"The year {year} in Roman numerals is {roman_year}")
```