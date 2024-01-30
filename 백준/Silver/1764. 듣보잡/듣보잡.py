n, m = map(int, input().split())
A, B = set(), set()
for case in range(n+m):
    if case < n:
        A.add(input())
    else:
        B.add(input())

result = sorted(A.intersection(B))
print(len(result))
for val in result:
    print(val)