test_case = int(input())

numbers = list(map(int, input().split()))
numbers = sorted(numbers)

cmd = int(input())
case = list(map(int, input().split()))

for num in case:
    left = 0
    right = len(numbers)-1
    flag = 0
    while True:
        mid = (left+right)//2
        if num == numbers[left] or num == numbers[right]:
            flag= 1
            break
        if num < numbers[mid]:
            right = mid
        elif num == numbers[mid]:
            flag = 1
            break
        elif num > numbers[mid]:
            left = mid
        if right-left == 1:
            break
    if flag == 1:
        print(1)
    else:
        print(0)