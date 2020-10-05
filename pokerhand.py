cards_arr = [w[0] for w in list(input().split(' '))]
strength = 1

# count occurance of every card in the list
for i in range(5):
    same_cards = cards_arr.count(cards_arr[i])
    strength = same_cards if same_cards > strength else strength

print(strength)