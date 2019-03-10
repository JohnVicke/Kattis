import sys
i = 1
for nrs in sys.stdin.readlines():
    nrs = [int(x) for x in nrs.split()]
    print('Case %d: %d %d %d' %(i , min(nrs[1:]), max(nrs[1:]), (max(nrs[1:]) - min(nrs[1:]))))
    i += 1
