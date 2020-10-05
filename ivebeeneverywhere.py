t = int(input())

for i in range(t):
    l = set()
    n = int(input())
    for j in range(n):
        c = input()
        if c not in l:
            l.add(c)
    print(len(l))
            