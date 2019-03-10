
dataset = int(input())
for i in range(dataset):
    k, n = [int(x) for x in input().split()]
    index = 0
    s1 = 0
    s2 = 0
    s3 = 0
    for j in range(n):
        index += 1
        s1 = s1 + index
        if index % 2 is not 0:
            s2 = s2 + index
        else:
            s3 = s3 + index

    print('testprin',k,s1,s2,s3)
