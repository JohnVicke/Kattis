# N = fish to sell
# M = mongos
# fish_w = weight of fishies
# fish = how many they want to buy
# monies = price/kg

n,m = [int(_) for _ in input().split()]
fish_w = [int(_) for _ in input().split()]

mongos = []
output = 0

for i in range(m):
    mongos.append([int(_) for _ in input().split()])

while len(fish_w) > 0 and len(mongos) > 0:
    mongo = mongos.pop(mongos.index(max(mongos, key=lambda x: x[1] )))
    f = fish_w.pop(fish_w.index(max(fish_w)))
    for i in range(mongo[0]):
        if len(fish_w) > 0:
            f = fish_w.pop(fish_w.index(max(fish_w)))
            output += f * mongo[1]
        else: 
            break


print(output)
