import sys
from bisect import bisect_left


input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
dp = [0]

for val in lst:
    if dp[-1] < val:
        dp.append(val)
    else:
        dp[bisect_left(dp, val)] = val

print(len(dp)-1)