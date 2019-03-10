
# Returns true if nr is prefix of other nr in a list of phone nrs

def is_prefix(l):
    for i in range(len(l)):
        nr_len = len(l[i])

        for j in range(i+1,len(l)):
            if l[i] == l[j][:nr_len]:
                return False
    return True

t = int(input())

for i in range(t):
    n = int(input())
    phone_nrs = []
    for i in range(n):
        nr = input()
        if nr in phone_nrs:
            consistent = False
            break

        phone_nrs.append(nr)

    print('NO') if not is_prefix(phone_nrs) else print('YES')
