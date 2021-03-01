import sys

while True: 
  jack, jill = [int(x) for x in sys.stdin.readline().split()]
  jack_cds = set(sys.stdin.readline() for i in range(jack))
  b = 0
  for i in range(jill):
    b += int(sys.stdin.readline()) in jack_cds

  print(b)
