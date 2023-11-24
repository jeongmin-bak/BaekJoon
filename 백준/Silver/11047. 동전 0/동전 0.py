import sys

input = sys.stdin.readline
n, k = map(int, input().split())
nlist=[int(input()) for i in range(n)]
nlist.sort(reverse=True)
cnt=0

for num in nlist:
    if k < num:
        continue
    cnt += k // num
    k = k % num

    if k == 0:
        break

print(cnt)