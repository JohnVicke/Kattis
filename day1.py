from pathlib import Path


def get_int(l):
    increase = l.strip("\n")
    return int(increase)


def change_frequency(output, finding, f):
    lines = f.split('\n')
    for line in lines:

        if line[:1] is '+':
            output = output + get_int(line[1:])

        else:
            output = output - get_int(line[1:])

        if output in frequencies and finding:
            print(output)
            break

        if not finding:
            frequencies.append(output)

    return output


file = Path('day1input.txt').read_text()

out = 0
frequencies = list()
searching = False
out = change_frequency(out, searching, file)
searching = True

while searching:
    out = change_frequency(out, searching, file)

print(out)
