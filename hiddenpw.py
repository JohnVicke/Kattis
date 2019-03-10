P,S = [line for line in input().split()]

set_index = 0
next_index = 1

looking_for = P[set_index]
next_in_set = P[next_index]

PASS = False

for c in S:
    if c == next_in_set:
        PASS = False
        break

    elif c == looking_for:

        set_index += 1
        next_index += 1

        if next_index < len(P):
            next_in_set = P[next_index]
        else:
            next_in_set = None

        if set_index == len(P):
            PASS = True
            break

        looking_for = P[set_index]

print('PASS') if PASS else print('FAIL')
