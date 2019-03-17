n = int(input())
nrs = []
for i in range(n):
    nrs.append(int(input()))

nrs.sort()
out = 0

while len(nrs) >= 3:
    out += nrs.pop()
    out += nrs.pop()
    nrs.pop()

while len(nrs) > 0:
    out += nrs.pop()

print(out)

