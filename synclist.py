test = -1 

while test != 0:
    test = int(input())
    l1 = []
    l2 = []
    for i in range(test):
        l1.append(int(input()))
    for i in range(test):
        l2.append(int(input()))

    copy = l1[:]
    l1.sort()     
    l2.sort()
    corr = {}
    for i in range(len(l1)):
        corr[l1[i]] = l2[i]
    
    for _ in copy:
        print( corr[_])
