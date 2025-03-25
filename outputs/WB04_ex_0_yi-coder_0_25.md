Here is a Python function that fulfills the given requirements:

```python
def intToRoman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    i = 0
    while  num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num
```
This function works by dividing the input number by each of the possible Roman numeral values, starting with the largest. For each value where the result is non-zero, it adds the corresponding symbol to the output string and subtracts the value from the total. It repeats this process until there are no more remaining values.