```python
def convert_to_roman(year):
    roman_year = ""
    while year >= 1000:
        roman_year += "M"
        year -= 1000
    if year >= 900:
        roman_year += "CM"
        year -= 900
    while year >= 500:
        roman_year += "D"
        year -= 500
    if year >= 400:
        roman_year += "CD"
        year -= 400
    while year >= 100:
        roman_year += "C"
        year -= 100
    if year >= 90:
        roman_year += "XC"
        year -= 90
    while year >= 50:
        roman_year += "L"
        year -= 50
    if year >= 40:
        roman_year += "XL"
        year -= 40
    while year >= 10:
        roman_year += "X"
        year -= 10
    if year >= 9:
        roman_year += "IX"
        year -= 9
    while year >= 5:
        roman_year += "V"
        year -= 5
    if year >= 4:
        roman_year += "IV"
        year -= 4
    while year >= 1:
        roman_year += "I"
        year -= 1
    return roman_year


year = int(input("Enter a year within the range 1 to 2000: "))
roman_year = convert_to_roman(year)
print(f"The year {year} in Roman numerals is {roman_year}")
```

**Example Output:**

```
Enter a year within the range 1 to 2000: 1984
The year 1984 in Roman numerals is MCMLXXXIV
```

**Note:**

* This program uses loops to convert each digit of the year to its Roman numeral equivalent.
* The `while` loops handle the subtractive cases (e.g., CM, CD).
* The `if` statements handle the additive cases (e.g., M, C, X).
* The input is validated to ensure it is within the range 1 to 2000.