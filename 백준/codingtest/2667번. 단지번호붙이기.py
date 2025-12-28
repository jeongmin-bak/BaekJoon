import sys

input = sys.stdin.readline
count = 0
N = int(input())
dx = [0,0,1,-1]
dy = [1,-1,0,0]

result = []
def dfs(x, y):
    global count

    if x < 0 or x >= N or y < 0 or y >= N:
        return
    if maps[x][y] == '1':
        count += 1
        maps[x][y] = '0'

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)


maps = list()
for i in range(N):
    maps.append(list(input()))

for i in range(N):
    for j in range(N):
        if maps[i][j] == '1':
            dfs(i, j)
            result.append(count)
            count = 0

result.sort()
print(len(result))
for k in result:
    print(k)