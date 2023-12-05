import re

with open("input_02.txt") as f:
    data = f.read().split("\n")

max_colors_dict = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def max_colors(color_list):
    for name, max_number in max_colors_dict.items():
        color = re.findall(rf"(\d+) {name}", color_list)
        if color and (int(color[0]) > max_number):
            return False
    return True


id_sum = 0
for lines in data:
    id_divider = lines.split(": ", maxsplit=1)
    games = id_divider[1].split("; ")
    validator = True
    for game in games:
        validator = max_colors(game)
        if not validator:
            break
    if validator:
        id_sum += int(id_divider[0].split()[1])

print(id_sum)
