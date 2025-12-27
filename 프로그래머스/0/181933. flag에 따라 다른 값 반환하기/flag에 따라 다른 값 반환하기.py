def solution(a, b, flag):

    answer = 0

    if flag:
        answer = int(a) + int(b)
    else:
        answer = int(a) - int(b)

    return answer