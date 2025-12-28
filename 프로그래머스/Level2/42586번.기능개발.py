from collections import deque
def solution(progresses, speeds):
    answer = []
    deploys = deque((100 - p + s -1) // s for p,s in zip(progresses, speeds) )
    while deploys:
        cur = deploys.popleft()
        cnt = 1

        while deploys and deploys[0] <= cur:
            deploys.popleft()
            cnt += 1

        answer.append(cnt)
    return answer

progresses, speeds = [93, 30, 55], [1, 30, 5] # 7,3,9
#progresses, speeds = [95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]
#progresses, speeds = [95], [4]
print(solution(progresses, speeds))