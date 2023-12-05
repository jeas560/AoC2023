import re
from functools import reduce

with open("input_02.txt") as f:
    data = f.read().split("\n")

color_name_list = {
    "red",
    "green",
    "blue",
}


def min_colorset(color_list):
    colorset_dict = {}
    for name in color_name_list:
        color_numbers = re.findall(rf"(\d+) {name}", color_list)
        if color_numbers:
            colorset_dict[f"{name}"] = max([int(color_number) for color_number in color_numbers])
    return colorset_dict


power_acumulated = 0
for lines in data:
    id_divider = lines.split(": ", maxsplit=1)
    games = id_divider[1]
    minimum_set_of_cubes = min_colorset(games)
    power = reduce((lambda x, y: x * y), [value for value in minimum_set_of_cubes.values()])
    power_acumulated += power

print(power_acumulated)

