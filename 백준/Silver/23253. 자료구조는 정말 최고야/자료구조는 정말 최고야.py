import sys

input = sys.stdin.readline
n, m = map(int, input().split())
Flag = True
for _ in range(m):
    x = int(input())
    dummy = list(map(int,input().split()))

    if dummy != sorted(dummy, reverse=True):
        Flag = False
        break

if Flag:
    print("Yes")
else:
    print("No")