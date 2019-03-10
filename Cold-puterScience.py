import sys

s = input()
index = 0

for i in s[1:].split(" "):
    i = int(i)
    if(i < 0):
        index = index + 1

print(index)
