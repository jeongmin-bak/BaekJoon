import sys
from collections import deque

input = sys.stdin.readline

cnt = 0
visited = []
def bfs(graph, start_node):
    global cnt
    need_visit = deque()
    need_visit.append(start_node)
    while need_visit:
        node = need_visit.popleft()
        if node == start_node and node in visited:
            cnt += 1
            return
        if node not in visited:
            visited.append(node)
            need_visit.append(graph[node])


for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    visited = []
    cnt = 0
    graph = dict()
    for i in range(1, n+1):
        graph[i] = data[i-1]

    for idx in range(1,n+1):
        if idx not in visited:
            bfs(graph, idx)
    print(cnt)