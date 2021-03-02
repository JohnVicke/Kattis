from functools import reduce
qol = 0
for i in range(int(input())):
  qol += reduce(lambda q, y: q*y, [float(_) for _ in input().split(" ")])

print(qol)