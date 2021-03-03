n = int(input())

for i in range(n):
  x = [int(_) for _ in input().split(" ")]
  k = x[0]
  oi = x[1:]
  print(sum(oi) - k + 1)

