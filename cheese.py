n,m = [int(x) for x in input().split()]
w = [int(x) for x in input().split()]

ps = []
ts = []

for i in range(m):
    p = [float(x) for x in input().split()]
    ts.append(p.pop())
    ps.append(p)

bi = p.index(max(p))

# 3 2
# 100 150 100
# 50.0 50.0 0.0 3.20 (200lbs)
# 0.0 50.0 50.0 2.80 (100lbs)
# ==> 920.0

# 200 50 150
# 20 80  0   5.0000000000000000000000000000000000000000000000000000000000001
# 80 20  0   5

# Innan allt
# Lös 2an
# Testa:
# Maxa alla
# Ta den som ger mest profit när den e maxad
# Fyll ut me nästa som går / den som ger mest profit