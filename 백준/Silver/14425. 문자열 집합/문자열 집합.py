n, m = map(int, input().split())

S = set()
for _ in range(n):
    S.add(input())

cnt = 0
for _ in range(m):
    data = input()
    if data in S:
        cnt += 1
print(cnt)