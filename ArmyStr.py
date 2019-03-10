def find_winner(mech_str, god_str):

    if max(god_str) >= max(mech_str):
        print('Godzilla')
    else:
        print('MechaGodzilla')


n = int(input())

for i in range(n):
    input()
    nr_minions_god, nr_minions_mech = map(int, input().split())
    god_str = [int(str1) for str1 in input().split()]
    mech_str = [int(str2) for str2 in input().split()]
    find_winner(mech_str, god_str)
