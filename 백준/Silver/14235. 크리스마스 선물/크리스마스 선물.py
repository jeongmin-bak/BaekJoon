from queue import PriorityQueue

n = int(input())
gift = PriorityQueue()
for case in range(n):
    alst = list(map(int, input().split()))
    if alst[0] == 0:
        if gift.empty():
            print(-1)
        else:
            print((-1)*gift.get())
    else:
        for buy in alst[1:]:
            gift.put((-1)*buy)