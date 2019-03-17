while True:
    n = int(input())
    if not n:
        break

    names = []
    for i in range(n):
        names.append(input())

    names.sort(key=lambda x: x[:2])
    print('\n'.join(names) + '\n')
