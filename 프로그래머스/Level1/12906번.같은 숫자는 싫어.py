from collections import deque
def solution(arr):
    queue = deque(arr)
    answer = [queue.popleft()]

    while queue:
        num = queue.popleft()
        if num != answer[len(answer)-1]:
            answer.append(num)

    return answer

arr_in = [4,4,4,3,3]
print(solution(arr_in))