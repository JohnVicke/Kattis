input = input()

previousChar = input[0]
outlist = previousChar

for s in input[1:]:
    if(previousChar is not s):
        outlist += s

    previousChar = s

print(outlist)
