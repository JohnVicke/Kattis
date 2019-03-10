import sys

for line in sys.stdin.readlines():
    p1, p2 = [int(x) for x in line.split()]
    print(abs(p1 - p2))
