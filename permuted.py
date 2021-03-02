def is_arithmethic(s):
  d = int(s[1]) - int(s[0])
  for i in range(len(s) - 1): 
    if not abs(int(s[i]) - int(s[i+1])) == d:
      return False 

  return True 

def compare(x,y):
  return int(x) - int(y)

n = int(input())

for i in range(n):
  seq = [_ for _ in input().split(" ")][1:]
  if is_arithmethic(seq):
    print("arithmethic")
  else:
    sorted_seq = sorted(seq, key=lambda t: abs(int(t[-1]) - int(t[0])))
    print(sorted_seq)
    print("permuted arithmetic") if is_arithmethic(sorted_seq) else print("non-arithmetic")
