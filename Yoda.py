w1 = list(input())
w2 = list(input())

if len(w1) < len(w2):
    w1.append(0)

def collision(w1, w2):
    i = 0
    leftover = list();
    for nr in w1:
        if(nr < w2[i]):
            continue
        elif(nr > w2[0]):
            leftover.append(nr)
        else:
            leftover.append(nr)
        i += 1
    return leftover

if not collision(w1, w2):
    print("YODA")
else:
    print(collision(w1,w2))

if not collision(w2, w1):
    print ("YODA")
else:
    print(collision(w2,1))
