n = int(input())

while n is not -1:
    distance = 0
    timeNow = 0

    for i in range(n):
        s,t = input().split()
        dist_per_pair = int(s) * (int(t) - int(timeNow))
        distance += dist_per_pair
        timeNow = t

    print(distance, 'miles')

    n = int(input())
