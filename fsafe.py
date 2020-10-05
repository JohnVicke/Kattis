t = int(input())
for i in range(t):
    n, m = [int(x) for x in input().split()] 
    visited = []
    pilots_trusted = 0
    for i in range(m):
        a, b = [int(x) for x in input().split()] 

        if i == 0: 
            visited.append(a)
            visited.append(b)
            pilots_trusted += 1
        else:
            if a not in visited and b in visited:
                visited.append(a)
                pilots_trusted += 1

            if b not in visited and a in visited:
                visited.append(b)
                pilots_trusted += 1
    print(pilots_trusted)



# 1
# 4 3
# 1 2
# 3 4
# 2 3