import random

graph = {}
bridges = []
for i in range(1, 11):
    graph[i] = [j for j in range(1, 11) if j != i]
    for j in graph[i]:
        if [i, j] not in bridges and [j, i] not in bridges:
            bridges.append([i, j])

print("Bridges:", bridges)

orig_bridge_count = len(bridges)

bridges = bridges[:len(bridges)//2]
print(f"{orig_bridge_count - len(bridges)} bridges broken")
new_graph = {}
for node in graph:
    new_graph[node] = [bridge for bridge in graph[node] if [node, bridge] in bridges or [bridge, node] in bridges]

print("Remaining bridges:", bridges)
print("New Graph:", new_graph)
