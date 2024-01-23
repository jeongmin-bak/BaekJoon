import sys

input = sys.stdin.readline

T = int(input())
for case in range(T):
    flag = True
    stack = []
    for s in input():
        if s == "(":
            stack.append(s)
        elif s == ")" and stack:
            stack.pop()
        elif s == ")" and len(stack) == 0:
            flag = False
            break
    if flag == False or stack:
        print("NO")
    else:
        print("YES")