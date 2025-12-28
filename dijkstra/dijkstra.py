import heapq

mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}


INF = int(1e9)

distances = {node: INF for node in mygraph}
distances['A'] = 0
print(distances)