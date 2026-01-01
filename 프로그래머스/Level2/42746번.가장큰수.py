
def solution(numbers):
    str_list = list(map(str, numbers))
    str_list.sort(key=lambda x: x * 3, reverse=True)
    answer = str(int(''.join(str_list)))
    return answer

numbers = [6, 10, 2,201]
numbers = [3, 30, 34, 5, 9]

print(solution(numbers))