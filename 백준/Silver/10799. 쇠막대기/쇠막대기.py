data = input()
stack = []
cnt = 0
for idx in range(len(data)):
    if data[idx] == "(":
        stack.append(data[idx])
    else:
        if data[idx-1] == "(":
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1
print(cnt)