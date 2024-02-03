n = int(input())

for _ in range(n):
    N, M = map(int, input().split())
    printer = []
    prior = list(map(int, input().split()))

    index = 0
    for value in prior:
        printer.append((value,index))
        index += 1

    tmp = printer.copy()
    cnt = 0

    while True:
        check = printer.pop(0)
        if all(check[0] >= x[0] for x in printer):
            cnt += 1
        else:
            printer.append(check)
        if tmp[M] not in printer:
            print(cnt)
            break