import sys
import heapq

n = int(sys.stdin.readline())
heap = []
answer = []

for i in range(n):
    x = int(sys.stdin.readline())

    if x == 0:
        if heap:
            num = (-1) * heapq.heappop(heap)
            answer.append(num)
        else:
            answer.append(0)

    else:
        heapq.heappush(heap, -x)

for i in answer:
    print(i)