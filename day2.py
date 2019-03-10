from pathlib import Path

file = Path('day2input.txt').read_text().split()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
duplicates = 0
triplets = 0

for line in file:
    freq = list()
    for c in alphabet:
        if line.count(c) == 2 or line.count(c) == 3:
            freq.append(line.count(c))

    if freq.count(2) > 0:
        duplicates += 1
    if freq.count(3) > 0:
        triplets += 1

print(duplicates * triplets)
