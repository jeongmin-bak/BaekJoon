import sys
from collections import deque

# 추가문제 : 인덱스 구하기
input = sys.stdin.readline

bars = deque()
n = int(input())

for _ in range(n):
    bars.append(int(input()))

std = bars.pop()
cnt = 1

#방법1
while bars:
    if bars[-1] > std:
       std = bars.pop()
       cnt += 1
    else:
        bars.pop()

print(cnt)