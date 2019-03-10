n,t = list(map(int, input().split()))
q = []

for i in range(n):
    c, ttl = list(map(int, input().split()))
    q.append([c,ttl])

# sorted list , s, richest first
s = sorted(q, key=lambda x: x[0], reverse=True)
out = 0

# see if spot in queue is taken to place people far back in queue
used = [0] * 47
for a in s:
    c = a[0]
    ttl = a[1]
    while t >= 0:
        if used[ttl] == 0:
             out += c
             used[ttl] = 1
             break
        t -= 1

print(out)
