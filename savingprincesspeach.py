found =  []
N, Y = [int(x) for x in input().split()]

for i in range(Y):
    found.append(int(input()))

for i in range(N):
    if i not in found:
        print(i)

print('Mario got %d of the dangerous obstacles.' %Y)
