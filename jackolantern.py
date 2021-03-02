from functools import reduce
print(reduce((lambda x, y: x*y), [int(x) for x in input().split(" ")]))