x = int(input())
n = int(input())
a = 0
for i in range(n):
    a += int(input())

avaiable = n*x
used = a

print(avaiable-used + x)
