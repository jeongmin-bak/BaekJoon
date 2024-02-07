import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    funcp = deque(input().rstrip())
    n = int(input())
    nums = deque(input().rstrip()[1:-1].split(","))

    if n == 0:
        nums = deque()
        
    if funcp.count('D') > len(nums):
        print("error")
        continue

    r_cnt = 0
    for cmd in funcp:
        if cmd == 'R':
            r_cnt += 1
        elif cmd == 'D':
            if r_cnt % 2 == 0:
                nums.popleft()
            else:
                nums.pop()

    if r_cnt % 2 == 0:
        print("[" + ",".join(nums) + "]")
    else:
        nums.reverse()
        print("[" + ",".join(nums) + "]")