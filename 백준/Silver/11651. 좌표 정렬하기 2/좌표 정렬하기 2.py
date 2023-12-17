import sys

input = sys.stdin.readline
n = int(input())
lst = []
for i in range(n):
    x, y = map(int, input().split())
    lst.append([y, x])

lst.sort()

for y,x in lst:
    print("{0} {1}".format(x, y))