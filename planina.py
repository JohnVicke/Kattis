rec = (lambda x: 2 if x == 0 else (2 * rec(x-1) -1))
print(rec(int(input()))**2)

