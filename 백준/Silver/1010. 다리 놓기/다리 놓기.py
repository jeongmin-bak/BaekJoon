cnt = int(input())

def combin(num):
    result = 1
    for i in range(1,num+1):
        result *= i
    return result
for case in range(cnt):
    n,m = map(int, input().split())
    answer = combin(m) // (combin(m-n) * combin(n))
    print(answer)