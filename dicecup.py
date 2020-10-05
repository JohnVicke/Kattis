n,m = [int(x) for x in input().split()]
[print(min(n,m)+i+1) for i in range(max(n,m)-min(n,m)+1)]