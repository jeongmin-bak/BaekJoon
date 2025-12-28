import sys

N = int(sys.stdin.readline())
nums = list(map(int, input().split()))
nums.sort()

M = int(sys.stdin.readline())
nums2 = list(map(int, input().split()))

answer = []
for target in nums2:
    start = 0
    flag = 0
    end = len(nums)

    while start < end:
        mid = (start+end) // 2
        if target == nums[mid] or target == nums[start] or target == nums[end-1]:
            flag = 1
            break
        elif target > nums[mid]:
            start = mid
        else :
            end = mid
        if end-start == 1:
            break
    answer.append(flag)

for i in answer:
    print(i)

