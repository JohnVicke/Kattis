t = int(input())
output = ''

def reverse(s):
  if len(s) == 0:
    return s
  else:
    return reverse(s[1:]) + s[0]

for i in range(t):
  rows, cols = [int(x) for x in input().split()]

  for j in range(rows):
    cols = input()

    if cols.count('*') == len(cols) or cols.count('.') == len(cols):
      output = ''.join((cols + '\n', output))

    else:
      output = ''.join((reverse(cols) + '\n', output))
  print('Test', (i+1))
  print(output.strip('\n'))
  output = ''
