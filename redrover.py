string = input()

all_sets = set()

length = len(string)

for i in range(length):
    for j in range(i, (length +1)):
        all_sets.add(string[i:j])

min_chars = float("inf")

for s in all_sets:
    copy = string.replace(s, "M")
    new_len = len(copy) + len(s)
    min_chars = new_len if new_len < min_chars else min_chars 

print(min_chars) if min_chars < len(string) else print(len(string))
