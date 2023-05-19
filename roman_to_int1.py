s = input("Roman?: ")
print(s)
def romanToInt(self, s: str) -> int:
    roman_table = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    number = 0
    last = "I"

    for numeral in s[::-1]:
        if roman_table[numeral] < roman_table[last]:
            number -= roman_table[numeral]
        else:
            number += roman_table[numeral]
        last = numeral
    return number




