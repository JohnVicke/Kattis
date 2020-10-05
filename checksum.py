def transform(str_nr):
    out = 0
    if int(str_nr) * 2 > 9:
        l = (list(str((int(str_nr) * 2))))
        for n in l:
            out += int(n)
    else:
        out = int(str_nr) * 2
    return out

for i in range(int(input())):
    line = input()
    luhns_sum = []
    index = 1
    for x in range(len(line)-1, -1, -1):
        if index % 2 == 0:
            luhns_sum.append(transform(line[x]))
        else: 
            luhns_sum.append(int(line[x]))
        index += 1
        
    print("PASS") if sum(luhns_sum) % 10 == 0 else print("FAIL")