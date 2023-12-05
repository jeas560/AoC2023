with open('input_01.txt') as f:
    data = f.read().split()

total = 0
for lines in data:
    digits_per_line = [digit for digit in lines if digit.isdigit()]
    extremes_sum = int(digits_per_line[0] + digits_per_line[-1])
    total += extremes_sum

print(total)
