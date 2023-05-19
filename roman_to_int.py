
roman_table = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000,
}

integer = 0

user_input = input("Roman Value?: ").strip().upper()

for i in range(len(user_input)):
    if user_input[i] in roman_table:
        if i + 1 < len(user_input) and roman_table[user_input[i]] < roman_table[user_input[i + 1]]:
            integer -= roman_table[user_input[i]]
        else:
            integer += roman_table[user_input[i]]
    else:
        print("Invalid statement!")

print("Integer: ", integer)