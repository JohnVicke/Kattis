# 0.10 $ per minute spent in park.
# for each enter/exit += exit - entry / 0.10

day = 0
while(True):
    try:
        data = input()
    except EOFError:
        break;

    if data.find("OPEN") != -1:
        day += 1

        


print(day)
