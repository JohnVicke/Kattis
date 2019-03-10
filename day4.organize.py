import os
from pathlib import Path

data = Path('day4.in.txt').read_text().split('\n')


def bubble_sort(l):
    for iter_num in range(len(l) - 1, 0, -1):
        for i in range(iter_num):
            if int(l[i][6:8]) > int(l[i + 1][6:8]):
                temp = l[i]
                l[i] = l[i + 1]
                l[i + 1] = temp


bubble_sort(data)
for line in data:
    Path('organizedata.txt').write_text(line)



