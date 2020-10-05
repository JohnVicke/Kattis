def is_even(a,b):
    return (a + b) % 2 == 0

def print_line(i,j):
    print("#", end="") if is_even(i,j) else print(".", end="")

m, n = [int(x) for x in input().split()]
u,l,r,d = [int(x) for x in input().split()]

strings = []

g_i = g_j = 0

for i in range(m):
    strings.append(input())

for i in range(u):
    g_i += 1
    for j in range(l + r + n):
        g_j += 1
        print_line(g_i, g_j)
    print()
    g_j = 0

for i in range(m):
    g_i += 1
    for j in range(l):
        g_j += 1
        print_line(g_i, g_j)
    print(strings.pop(0), end="")

    if n % 2 != 0:
        g_j += 1

    for j in range(r):
        g_j += 1
        print_line(g_i, g_j)
    print()

    g_j = 0

for i in range(d):
    g_i += 1
    for j in range(l + r + n):
        g_j += 1
        print_line(g_i, g_j)
    print()
    g_j = 0

