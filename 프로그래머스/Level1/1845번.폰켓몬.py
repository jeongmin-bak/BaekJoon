from collections import Counter

# 숫자의 갯수 >  자리 -> 자리 수
# 숫자의 갯수 = 자리 -> 동일
# 숫자의 갯수 Unique < 자리 -> 숫자의 갯수

def solution(nums):
    answer = len(nums) // 2
    nums_cnt = Counter(nums)
    cnt = len(nums_cnt.keys())

    if cnt < answer:
        answer = cnt

    return answer

li = [3,3,3,2,2,2]
print(solution(li))