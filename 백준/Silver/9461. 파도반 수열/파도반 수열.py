import sys

input = sys.stdin.readline

T = int(input())
lst = [1,1,1]
i = 0
for case in range(T):
    n = int(input())
    i = len(lst)-3
    while True:
        if len(lst) >= n:
            print(lst[n-1])
            break
        lst.append(lst[i]+lst[i+1])
        i += 1