n = int(input())
for i in range(n):
    line = input()
    if line.find('Simon says') != -1:
        print(line[11:])
