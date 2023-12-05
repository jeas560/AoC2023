with open("input_01.txt") as f:
    data = f.read().split()

digits = [
    "one",
    "1",
    "two",
    "2",
    "three",
    "3",
    "four",
    "4",
    "five",
    "5",
    "six",
    "6",
    "seven",
    "7",
    "eight",
    "8",
    "nine",
    "9",
]


def first_digit(code):
    first = len(code)
    value = "0"
    for index, digit in enumerate(digits):
        first_temp = code.find(digit)
        if (first_temp > -1) and (first_temp < first):
            first = first_temp
            if not index % 2:
                value = digits[index + 1]
            else:
                value = digits[index]
    return value


def last_digit(code):
    last = -1
    value = "0"
    for index, digit in enumerate(digits):
        last_temp = code.rfind(digit)
        if (last_temp > -1) and (last_temp > last):
            last = last_temp
            if not index % 2:
                value = digits[index + 1]
            else:
                value = digits[index]
    return value


total = 0

for lines in data:
    first_value = first_digit(lines)
    last_value = last_digit(lines)
    extremes_sum = int(first_value + last_value)
    total += extremes_sum

print(total)
