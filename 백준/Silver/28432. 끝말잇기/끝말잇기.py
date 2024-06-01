n = int(input())
S = []
for _ in range(n):
    S.append(input())

if '?' in S:
    idx = S.index('?')
    # ?가 맨처음에 오는경우
    if idx == 0:
        first_char = ""
    else:
        first_char = S[idx-1][-1]

    if idx == len(S)-1:
        last_char = ""
    else:
        last_char = S[idx+1][0]

m = int(input())
for _ in range(m):
    candidate = input()
    if candidate not in S:
        if (not first_char or candidate[0] == first_char) and (not last_char or candidate[-1] == last_char):
            print(candidate)