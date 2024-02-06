import sys
from collections import deque

input = sys.stdin.readline
stack1 = deque(input().rstrip())
M = int(input())
cursor = len(stack1)
stack2 = deque()
for _ in range(M):
    command = list(map(str, input().split()))
    if command[0] == 'P':
        if cursor == len(stack1):
            stack1.append(command[1])
            cursor += 1
    elif command[0] == "L":
        if cursor > 0:
            stack2.appendleft(stack1.pop())
            cursor -= 1
    elif command[0] == "D" and stack2:
        stack1.append(stack2.popleft())
        cursor += 1
    elif command[0] == "B":
        if cursor > 0:
            stack1.pop()
            cursor -= 1

print(''.join(stack1) + ''.join(stack2))