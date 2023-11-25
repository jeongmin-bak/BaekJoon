n = int(input())
nlist = list(map(int, input().split()))
nlist = sorted(nlist)

sum = 0
result = 0
for num in nlist:
    sum += num
    result += sum

print(result)