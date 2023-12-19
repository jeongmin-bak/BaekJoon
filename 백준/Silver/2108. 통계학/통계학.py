import sys
from collections import Counter

input=sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()

print(round(sum(nums) / n))  # 산술평
print(nums[(len(nums)) // 2])

if len(nums) <= 1:
    print(nums[0])
else:
    cnts = sorted(Counter(nums).items(), key=lambda x: x[1], reverse=True)
    if cnts[0][1] == cnts[1][1]:
        print(cnts[1][0])
    else:
        print(cnts[0][0])

print(nums[n-1] - nums[0])