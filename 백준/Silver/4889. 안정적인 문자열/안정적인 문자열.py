answer = []
while True:
    data = input()
    if '-' in data:
        break

    cnt, stack = 0, []
    for i in range(len(data)):
        if not stack and data[i] == '}':
            cnt += 1
            stack.append('{')
        elif stack and data[i] == '}':
            stack.pop()
        else:
            stack.append(data[i])

    cnt += len(stack) // 2
    answer.append(cnt)

for i in range(len(answer)):
    print(i+1, '. ', answer[i], sep='')