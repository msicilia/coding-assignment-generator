
import re

def convert_to_roman(year):
    if not 1 <= year <= 2000:
        raise ValueError("Year must be between 1 and 2000")
    
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
        1: "I"
    }
    
    roman_numeral = ""
    for key, value in roman_numerals.items():
        while year >= key:
            roman_numeral += value
            year -= key
            
    return roman_numeral

def test(year, expected):
    try:
        actual = convert_to_roman(year)
        assert actual == expected, f"Expected {expected}, but got {actual}"
    except Exception as e:
        assert False, f"Unexpected error: {e}"
    
test(1, "I")
test(4, "IV")
test(5, "V")
test(9, "IX")
test(10, "X")
test(40, "XL")
test(50, "L")
test(90, "XC")
test(100, "C")
test(400, "CD")
test(500, "D")
test(900, "CM")
test(1000, "M")
try:
    test(-1, "I")
except ValueError as e:
    assert str(e) == "Year must be between 1 and 2000", f"Unexpected error message: {str(e)}"
    
try:
    test(2001, "I")
except ValueError as e:
    assert str(e) == "Year must be between 1 and 2000", f"Unexpected error message: {str(e)}"