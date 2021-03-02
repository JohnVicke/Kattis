t = int(input())

for i in range(t):
  n = input()
  index = len(n) - 1
  while index > 0 and n[index] == "0":
    index -= 1
  if index == 0 and n[index] == "1":
    print("0")
  else:
    n_list = [char for char in n]
    nr_to_subtract = str(int(n_list[index]) - 1)
    n_list[index] = nr_to_subtract
    print(int("".join(n_list)))
