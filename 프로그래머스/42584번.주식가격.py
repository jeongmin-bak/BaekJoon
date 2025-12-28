from collections import deque
import sys


def solution(prices):
    answer = []

    for j in range(len(prices)):
        num = prices.popleft()
        cnt = 0

        for x in range(0, len(prices)):
            if num <= prices[x]:
                cnt += 1
        answer.append(cnt)

    return answer

prices_in = list(map(int, sys.stdin.readline().split()))
prices_in = deque(prices_in)
print(solution(prices_in))
