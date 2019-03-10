import sys
from pathlib import Path
file = Path('day2input.txt').read_text().split()
first = file[0]

counter = 0
searching = True
line = 0
output = ''

while searching:
    line += 1
    for i in range(1, len(file)):
        second = file[i]
        if second is not first:
            for j in range(len(first)):
                if counter > 1:
                    output = ''
                    counter = 0
                    break
                if first[j] != second[j]:
                    counter += 1
                    output = first.replace(first[j], '')

            if counter == 1:
                print(output)
                sys.exit(0)

    first = file[line]

print(counter)