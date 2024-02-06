import sys
from collections import deque

test_cases = int(input())

for case in range(test_cases):
    cmd = sys.stdin.readline().rstrip()
    
    n = int(input())
    dq = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    
    if n == 0:
        dq = deque()

    flag = 0
    rev = 0
    for j in cmd:
        if j == 'R':
            rev += 1
        elif j == 'D':
            if len(dq) < 1:
                flag = 1
                print("error")
                break
            else:
                if rev % 2 == 0:
                    dq.popleft()
                else:
                    dq.pop()
    if flag == 0:
        if rev % 2 == 0:
            print("[" + ",".join(dq) + "]")
        else:
            dq.reverse()
            print("[" + ",".join(dq) + "]")