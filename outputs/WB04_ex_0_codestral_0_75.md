 Thought:
Since we are not allowed to use data structures other than basic iterations of sequences in loops, a simple approach would be to create a loop that subtracts the largest possible Roman numeral values from the input number and appends their corresponding Roman numerals to the result string. We can define these values and their corresponding Roman numerals as two arrays, and use indices to keep track of which value we are currently subtracting and converting.

   Code:
```py
def int_to_roman(input):
    # Define arrays for Arabic numbers and their corresponding Roman numerals
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    # Initialize an empty string to store the Roman numeral representation
    roman_numeral = ''

    # Loop through the values and subtract them from the input number, appending their corresponding Roman numerals to the result string
    i = 0
    while input > 0:
        while input >= values[i]:
            roman_numeral += numerals[i]
            input -= values[i]
        i += 1

    # Return the final Roman numeral representation
    return roman_numeral

# Test the function with some example inputs
print(int_to_roman(1985))  # Output: MCMLXXXV
print(int_to_roman(2021))  # Output: MMXXI
```