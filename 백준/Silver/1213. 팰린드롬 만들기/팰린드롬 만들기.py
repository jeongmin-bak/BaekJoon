from collections import Counter

def palindrome(word):
    ans = ""
    word = Counter(word)
    word_set = list(word.keys())
    word_set.sort() # 출력이 사전순임으로 정렬
    word_odd = [w for w in word_set if word[w]%2 != 0] #문자열의 길이가 홀수 : 해당문자열을 찾아서 list에 저장]

    for w in word_set:
        ans += w * (word[w] // 2)

    if word_odd:
        ans = ans + word_odd[0] + ans[::-1]
    else:
        ans = ans + ans[::-1]

    return str(''.join(ans))

n = input()
counter_n = Counter(n)
check_odd = [1 if i%2!=0 else 0 for i in counter_n.values()] # Counter 객체의 values 값 저장
if (len(n)%2==0 and sum(check_odd)==0) or (len(n)%2!=0 and sum(check_odd)==1):
    #팰린드롬 문자열로 변형가능 문자열 길이가 짝수 원소의 갯수가 홀수개인 원소가 0
    # 팰린드롬 문자열 길이가 홀수 원소의 갯수가 홀수개인 원소 갯수 1개인 경우
    print(palindrome(n))
else:
    print("I'm Sorry Hansoo")