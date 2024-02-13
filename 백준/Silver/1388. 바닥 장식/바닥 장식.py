import sys

input = sys.stdin.readline
# 세로길이 = n, 가로길이 = m
n,m = map(int, input().split())
floor = [list(input().rstrip()) for _ in range(n)]

# 방문하기전 노드들은 False로 초기화
visited = [[False] * m for _ in range(n)]
cnt = 0
# - 가 인접해 있고 같은 행에 있다면 두 개는 같은 나무 판자
# | 가 인접해 있고 같은 열에 있다면 두 개는 같은 나무 판자
def dfs(i, j, tile):
    global cnt
    while True:
        if i >= n or j >= m or floor[i][j] != tile:
            cnt += 1
            break
        if floor[i][j] == tile and visited[i][j] == False:
            visited[i][j] = True
            if tile == '-':
                j += 1
            else:
                i += 1

for i in range(n):
    for j in range(m):
        if visited[i][j] == False:
            dfs(i, j, floor[i][j])

print(cnt)