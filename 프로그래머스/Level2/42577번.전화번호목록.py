## 숫자를 정렬하여 비교할 숫자를 줄임
## 접두사인지 판별한 후 포함되어있지 않으면 서로 다른 숫자 break
## 값이 이미 False이면 그만 for문 해도됨

def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    for x in range(0, len(phone_book)-1):
        for y in range(x+1, len(phone_book)):
            if phone_book[y].startswith(phone_book[x]) :
                answer = False
                return answer
            else:
                break
        if answer == False:
            break
    return answer

li = ["12","123","1235","567","88"]
print(solution(li))