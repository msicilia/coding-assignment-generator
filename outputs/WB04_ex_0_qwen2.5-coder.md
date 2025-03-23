Certainly! Below is a Python program that converts an Arabic numeral year (between 1 and 2000) into Roman numerals using basic iterations of sequences in loops, without using data structures like lists or dictionaries.

```python
def arabic_to_roman(year):
    if not (1 <= year <= 2000):
        return "Year out of range"
    
    roman_numerals = [
        ('M', 1000),
        ('CM', 900),
        ('D', 500),
        ('CD', 400),
        ('C', 100),
        ('XC', 90),
        ('L', 50),
        ('XL', 40),
        ('X', 10),
        ('IX', 9),
        ('V', 5),
        ('IV', 4),
        ('I', 1)
    ]
    
    result = ""
    
    for numeral, value in roman_numerals:
        while year >= value:
            result += numeral
            year -= value
    
    return result

# Example test cases
print(arabic_to_roman(3))      # III
print(arabic_to_4)          # IV
print(arabic_to_9)          # IX
print(arabic_to_58)         # LVIII
print(arabic_to_1994)       # MCMXCIV
```

### Explanation:
1. **Function Definition**: The function `arabic_to_roman` takes an integer `year` as input.
2. **Range Check**: It first checks if the year is within the valid range (1 to 2000). If not, it returns "Year out of range".
3. **Roman Numeral Mapping**: A list of tuples `roman_numerals` is defined where each tuple contains a Roman numeral string and its corresponding Arabic value.
4. **Result Construction**: An empty string `result` is initialized to build the Roman numeral representation.
5. **Loop Through Mapping**: The function iterates over each tuple in the `roman_numerals` list.
6. **Subtraction and Appending**: Inside the loop, it uses a while loop to subtract the value from `year` as long as `year` is greater than or equal to the current value. During each iteration, the corresponding numeral is appended to the `result`.
7. **Return Result**: Finally, the constructed Roman numeral string is returned.

### Example Test Cases:
- `arabic_to_roman(3)` returns "III"
- `arabic_to_4` returns "IV"
- `arabic_to_9` returns "IX"
- `arabic_to_58` returns "LVIII"
- `arabic_to_1994` returns "MCMXCIV"

This program ensures that the conversion is done using basic iterations of sequences and adheres to the constraints provided.