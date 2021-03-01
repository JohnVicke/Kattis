w = int(input())
n = int(input()) 
area = 0
for i in range(n):
  wi, li = [int(_) for _ in input().split(" ")]
  area += wi * li

print(int(area/w))