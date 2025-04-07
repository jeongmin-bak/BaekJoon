import sys
sys.setrecursionlimit(10**6)

# 1. 값 입력 받기
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 2. 가능한 높이 옵션 추출
height_info = set(sum(arr, []))
directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

# 3. dfs 함수 정의
def dfs(x, y, limit, visited):
    # 방문 처리
    visited[x][y] = True 
    # 상하좌우 4방향 확인
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        # 예외 조건 미리 확인
        if nx>=0 and nx<n and ny>=0 and ny<n:
            if not visited[nx][ny] and arr[nx][ny] > limit:
                dfs(nx, ny, limit, visited)
    return True


max_answer = 1 # 물에 잠기지 않는 경우

# 4. 높이 옵션 별 DFS 알고리즘 적용
for height in height_info:
    visited = [[False]*n for _ in range(n)]
    answer = 0  
    for i in range(n):
        for j in range(n):
            if arr[i][j]>height and not visited[i][j]:
                if dfs(i, j, height, visited):
                    answer += 1 # 개수 카운팅
    # 높이 옵션 중 최대값 탐색
    max_answer = max(max_answer, answer)

print(max_answer)