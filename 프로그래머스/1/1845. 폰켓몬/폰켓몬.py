from collections import Counter

def solution(nums):
    answer = len(nums) // 2
    nums_cnt = Counter(nums)
    cnt = len(nums_cnt.keys())

    if cnt < answer:
        answer = cnt

    return answer