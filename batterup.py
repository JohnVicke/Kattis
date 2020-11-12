r = [input().split(' ') for i in range(2)]
print(sum(filter(lambda a: a >= 0,[int(x) for x in r[1:][0]])) / len(list(filter(lambda a : int(a) >= 0, r[1:][0]))))

