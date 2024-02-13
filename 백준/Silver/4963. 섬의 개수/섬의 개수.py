import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x, y):
    dx = [-1,1,0,0,-1,1,1,-1]
    dy = [0,0,-1,1,-1,1,-1,1]
    for i in range(8):
        nx = dx[i] + x
        ny = dy[i] + y
        if (0 <= nx < h) and (0 <= ny < w):
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                dfs(nx, ny)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = []
    cnt = 0

    for _ in range(h):
        graph.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)