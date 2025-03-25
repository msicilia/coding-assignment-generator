```
year = int(input("Enter a year in Arabic numerals: "))
if 1 <= year <= 2000:
    roman_numeral = ""
    if year >= 1000:
        roman_numeral += "M" * (year // 1000)
        year %= 1000
    if year >= 500:
        roman_numeral += "D" * (year // 500)
        year %= 500
    if year >= 100:
        roman_numeral += "C" * (year // 100)
        year %= 100
    if year >= 50:
        roman_numeral += "L" * (year // 50)
        year %= 50
    if year >= 10:
        roman_numeral += "X" * (year // 10)
        year %= 10
    if year >= 5:
        roman_numeral += "V" * (year // 5)
        year %= 5
    if year == 4 or year == 9:
        roman_numeral += "IV"
    elif year == 40 or year == 90:
        roman_numeral += "XL"
    elif year == 400 or year == 900:
        roman_numeral += "CD"
    else:
        roman_numeral += str(year)
    print(roman_numeral)
else:
    print("Invalid year")
```