from collections import deque
n,w,L = map(int, input().split())
wait_truck = deque(map(int, input().split()))

enter = deque()
for _ in range(w):
    enter.append(0)
idx = 0
cnt = 0

while idx < n:
    enter.popleft()

    if sum(enter) + wait_truck[idx] <= L and len(enter) <= w:
        enter.append(wait_truck[idx])
        idx += 1
        cnt += 1
    else:
        cnt += 1
        enter.append(0)
cnt += len(enter)
print(cnt)