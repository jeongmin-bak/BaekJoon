import sys

input = sys.stdin.readline
n,c = map(int,input().split())

lst = []
for _ in range(n):
    x = int(input())
    lst.append(x)

lst.sort()
def install_router(lst, C):

    start = 1
    end = lst[-1] - lst[0]
    gap = 0

    while start <= end:
        mid = (start+end) // 2

        cnt = 1
        cur = lst[0]

        for i in range(1, len(lst)):
            if lst[i] >= cur + mid:
                cur = lst[i]
                cnt += 1

        if cnt >= C:
            gap = mid
            start = mid + 1
        else:
            end = mid - 1
    return gap

print(install_router(lst,c))