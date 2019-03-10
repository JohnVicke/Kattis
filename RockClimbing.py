def least_energy(rows):
    rows = rows[::-1]

x,y = [int(x) for x in input().split()]
e = input()
rows = list()
for i in range(x):
    rows.append([int(x) for x in input().split()])
    print('row ', i , ' is ',rows)

s = input()
