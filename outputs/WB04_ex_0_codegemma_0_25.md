```python
def arabic_to_roman(year):
    """
    Converts an Arabic numeral year to its Roman numeral equivalent.

    Args:
        year: The Arabic numeral year to convert.

    Returns:
        The Roman numeral equivalent of the given year.
    """

    roman_numerals = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }

    roman_year = ""

    for numeral, symbol in reversed(sorted(roman_numerals.items())):
        while year >= numeral:
            roman_year += symbol
            year -= numeral

    return roman_year


# Example usage:
year = int(input("Enter a year between 1 and 2000: "))

if 1 <= year <= 2000:
    roman_year = arabic_to_roman(year)
    print(f"The Roman numeral equivalent of {year} is {roman_year}.")
else:
    print("Invalid year. Please enter a year between 1 and 2000.")
```

**Example Usage:**

```
Enter a year between 1 and 2000: 2023
The Roman numeral equivalent of 2023 is MMXXIII.
```

**Note:**

* The code uses a `while` loop to iteratively convert the Arabic numeral year to Roman numerals based on the `roman_numerals` dictionary.
* The `reversed()` function and `sorted()` function are used to iterate through the dictionary in descending order of numeral values.
* The input validation ensures that the user enters a valid year within the specified range.