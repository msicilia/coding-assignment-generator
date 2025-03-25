[PYTHON]
def roman_numeral(year):
    if year < 1 or year > 2000:
        return None
    num = ["I", "V", "X", "L", "C", "D", "M"]
    value = [1, 5, 10, 50, 100, 500, 1000]
    roman_numeral = ""
    for i in range(len(num)):
        while year >= value[i]:
            year -= value[i]
            roman_numeral += num[i]
    return roman_numeral
[/PYTHON]
