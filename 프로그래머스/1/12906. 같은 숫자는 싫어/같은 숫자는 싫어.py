from collections import deque
def solution(arr):
    queue = deque(arr)
    answer = [queue.popleft()]

    while True:
        num = queue.popleft()
        if num != answer[len(answer)-1]:
            answer.append(num)
        if len(queue) == 0:
            break

    return answer