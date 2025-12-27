from collections import deque
def solution(progresses, speeds):
    answer = []
    deploys = deque()

    for i in range(len(progresses)):
        x = (100 - progresses[i]) // speeds[i]
        y = 1 if (100 - progresses[i]) % speeds[i] > 0 else 0
        deploy = x + y
        deploys.append(deploy)
    print(deploys)
    start_idx, end_idx, cnt = 0, 0, 0

    while end_idx < len(deploys):
        if deploys[start_idx] < deploys[end_idx]:
            answer.append(end_idx-start_idx)
            start_idx = end_idx
            cnt = 0
        else:
            end_idx += 1
            cnt += 1

    if (len(deploys) == 1):
        answer.append(deploys[0])
    else :
        answer.append(cnt)
    return answer