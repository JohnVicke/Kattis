n = int(input())

for i in range(n):
    road_name = input()
    nr_buildings_str = input()
    nr_buildings = int(nr_buildings_str.split()[0])
    
    houses = []
    nrs = {}

    while len(houses) < nr_buildings - 1:
        numbers = input()
        print("in -> ", numbers)
        if "+" in numbers:
            start, end, ival = [int(x) for x in numbers[1:].split()]
            for j in range(start,end,ival):
                houses.append(j)
            houses.append(end)
        else:
            houses.append(int(numbers))
        

    print(road_name)
    print(nr_buildings)


# 101 103 105 .... 125 
# 275                               --> list 
# 100 200 300 400 500 ... 900


# nr of 0, 1, 2 ,3 , 4 ,5 ..  9