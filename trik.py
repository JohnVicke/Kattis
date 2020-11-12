
i = input()
start = [1,0,0]
for c in i:
  if c is 'A':
    temp=start[0]
    start[0]=start[1]
    start[1]=temp

  elif c is 'B':
    temp = start[1]
    start[1] = start[2]
    start[2] = temp
  
  else:
    temp = start[2]
    start[2] = start[0]
    start[0] = temp

print(start.index(1) + 1)