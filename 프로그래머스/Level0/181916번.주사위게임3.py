from collections import Counter
def solution(a, b, c, d):

    answer = 0

    li = [a,b,c,d]
    cnt_li = Counter(li)
    cnt_tuple = cnt_li.most_common()

    keys = list(cnt_li.keys())
    values = list(cnt_li.values())
    if(len(keys) == 1): # keys값이 1개이면 Count가 4일것
        answer = keys[0] * 1111
    elif(len(keys) == 2):
        if values[0] == values[1]:
            answer = (keys[0] + keys[1]) * abs(keys[0]-keys[1])
        else:
            answer = (10 * cnt_tuple[0][0] + cnt_tuple[1][0]) ** 2
    elif(len(keys) == 4):
        answer = min(li)
    else:
        answer = cnt_tuple[1][0] * cnt_tuple[2][0]

    return answer


#a, b, c, d = 2,2,2,2
#a, b, c, d = 4,1,4,4
#a, b, c, d = 6, 3, 3, 6
#a, b, c, d = 2, 5, 2, 6
a, b, c, d = 6, 4, 2, 5
print(solution(a,b,c,d))