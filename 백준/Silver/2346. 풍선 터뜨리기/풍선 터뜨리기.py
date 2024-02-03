from collections import deque
n = int(input())

cards = map(int, input().split())

ballons = deque()
for idx, card in enumerate(cards):
    ballons.append((idx+1, card))

idx = 0
while ballons:
    value, step = ballons.popleft()
    print(value)
    if step > 0:
        ballons.rotate(-(step-1))
    else:
        ballons.rotate(-step)