def solution(a, b, flag):

    answer = 0

    if flag:
        answer = int(a) + int(b)
    else:
        answer = int(a) - int(b)

    return answer

a, b, flag = input().split()
print(solution(a, b, flag))