import sys

input = sys.stdin.readline
n, m = map(int, input().split())
cards = list(map(int, input().split()))
sum = 0
for i in range(n):
    for j in range(i+1, n):
        for r in range(j+1, n):
            if cards[i] + cards[j] + cards[r] > m:
                continue
            else:
                sum = max(sum, cards[i] + cards[j] + cards[r])

print(sum)