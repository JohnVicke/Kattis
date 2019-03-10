from pathlib import Path
from collections import defaultdict


def get_coordinates(left, top, w, h):

    x = left + 1
    y = top + 1
    start_x = x
    start_y = y
    out = 0

    for i in range(start_y, start_y + h):
        y = i

        for j in range(start_x, start_x + w):
            x = j

            if y in coordinates[x] and y not in counted[x]:
                counted[x].append(y)
                out += 1
            else:
                coordinates[x].append(y)

    return out


claims = Path('day3in.txt').read_text().split('\n')
counter = 0
coordinates = defaultdict(list)
counted = defaultdict(list)

for claim in claims:
    split = claim.split('@')
    shift = split[1].split(',')
    pos_from_left = int(shift[0].lstrip().strip())
    shift = shift[1].split(':')
    pos_from_top = int(shift[0].strip().lstrip())
    shift = shift[1].split('x')
    width = int(shift[0].lstrip().strip())
    height = int(shift[1].lstrip().strip())
    counter += get_coordinates(pos_from_left, pos_from_top, width, height)

print(counter)

