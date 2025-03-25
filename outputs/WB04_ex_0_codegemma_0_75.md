```python
def convert_to_roman(year):
    """
    Converts an Arabic year to Roman numerals.

    Args:
        year: The year to convert.

    Returns:
        The Roman numeral equivalent of the year.
    """

    # Predefined Roman numeral mappings
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

    roman_numeral = ""

    # Iterate through the Roman numeral mappings in descending order
    for numeral, symbol in sorted(roman_numerals.items(), reverse=True):
        while year >= numeral:
            roman_numeral += symbol
            year -= numeral

    return roman_numeral


# Example usage
year = int(input("Enter a year between 1 and 2000: "))

roman_numeral = convert_to_roman(year)
print(f"The Roman numeral equivalent of {year} is {roman_numeral}")
```

**Example Output:**

```
Enter a year between 1 and 2000: 1984
The Roman numeral equivalent of 1984 is MCMLXXXIV
```

**Explanation:**

* The `convert_to_roman()` function takes a year as input and converts it to Roman numerals.
* It uses a dictionary to store the Roman numeral mappings.
* It iterates through the dictionary in descending order of numeral value.
* For each numeral, it checks if the year is greater than or equal to it.
* If so, it adds the corresponding Roman numeral symbol to the `roman_numeral` variable and subtracts the numeral from the `year`.
* The loop continues until all numerals have been checked.
* The function returns the `roman_numeral` variable.

**Note:**

* The code does not use any data structures other than the dictionary.
* It uses loops to iterate through the Roman numeral mappings.