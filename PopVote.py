n = int(input())

for i in range(n):
    nr_candidates = int(input())
    majority_winner = 0

    for j in range(nr_candidates)[2:]:
        print('i inside for j loop' , i)
