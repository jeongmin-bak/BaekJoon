import sys

input = sys.stdin.readline
n = int(input())
result = 0
for i in range(1, n+1):
    num = i;
    sum = 0
    while num != 0:
        sum += num % 10
        num = num // 10

    if (i + sum) == n:
        result = i
        break

print(result)