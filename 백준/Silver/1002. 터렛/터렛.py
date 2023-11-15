import sys

input = sys.stdin.readline

n = int(input())

for case in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = (x2-x1)**2 + (y2-y1)**2
    lst = []
    if(x1==x2) and (y1==y2) and (r1==r2):
        lst.append(-1)
    elif (distance > (r1+r2)**2) or (distance < (r2-r1)**2):
        lst.append(0)
    elif (distance == (r2-r1)**2) or (distance == (r1+r2)**2):
        lst.append(1)
    else:
        lst.append(2)

    print(lst[0])