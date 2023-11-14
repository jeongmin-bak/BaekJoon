T = int(input())

for i in range(T):
    start, end = map(int, input().split())

    d = end - start

    n = 0

    while True:
        if d <= n * (n + 1):
            break
        n += 1

    if d <= n ** 2:
        print(n * 2 - 1)

    else:
        print(n * 2)