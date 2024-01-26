from collections import deque

n, m = map(int, input().split())
idxs= list(map(int, input().split()))

dq = deque([i for i in range(1, n+1)])
cnt = 0

for idx in idxs:
    while True:
        if idx == dq[0]:
            dq.popleft()
            break
        elif dq.index(idx) > len(dq)/2:
            while dq[0] != idx:
                dq.appendleft(dq.pop())
                cnt += 1
        else:
            while dq[0] != idx:
                dq.append(dq.popleft())
                cnt += 1
print(cnt)