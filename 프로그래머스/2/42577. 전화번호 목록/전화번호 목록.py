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