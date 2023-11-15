
n = int(input())

for case in range(n):
    data = input()
    stack = []
    flag = True
    for val in data:
        if val == "(":
            stack.append(val)
        elif val == ")" and stack:
            stack.pop()
        elif val == ")" and len(stack) == 0:
            flag = False
            break

    if flag == False or stack:
        print("NO")
    else:
        print("YES")