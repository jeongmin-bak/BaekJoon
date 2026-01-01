import math
from itertools import permutations

def solution(numbers):
    answer = 0
    num_list = set(numbers)

    print(num_list)

    for x in permutations(num_list, len(num_list)):
        num = ''.join(x)
        num_list.append(num)
    num_list = list(map(int, num_list))
    print(num_list)
    for x in num_list:
        if x < 2:
            continue
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                continue
        answer += 1

    return answer

numbers = '011'
print(solution(numbers))