N = int(input())
S = list(map(str, input()))

stack = []
result = 0

for i in range(len(S)):
    if len(stack) == 0 or stack[-1] == S[i]:
        stack.append(S[i])
    else:
        if len(stack) != 0:
            stack.pop()
    result = max(result, len(stack))

if len(stack) == 0:
    print(result)
else:
    print(-1)
