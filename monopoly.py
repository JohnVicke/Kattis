class Node:
    def __init__(self):
        self.property = None
        self.salary = None
        self.Tax = None

# Nr of nodes & edges, max nr of turns / player, starting node of Alob and Bice
N,M,K,sa,sb = list(map(int, input().split()))
edges = []

for i in range(M):
    u, v = list(map(int, input().split()))
    edges.append([u,v])

for i in range(N):
    # Salary , tax or property
    pass
