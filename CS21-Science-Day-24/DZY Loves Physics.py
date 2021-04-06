nodes, edges = map(int, input().split())
nodesValues = list(map(int,input().split()))
density = 0
total = 0
for i in range(edges):
    node1, node2, edgeValue = map(int, input().split())
    total = (nodesValues[node2-1] + nodesValues[node1-1])/edgeValue
    if total > density:
        density = total
print(density)
