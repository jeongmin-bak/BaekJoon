dic = {
    ")":"(",
    "]":"["
}
def input_check():
    data = input()

    if data.endswith("."):
        return data

while True:
    data = input_check()
    if data == '.':
        break
    stack = []
    flag = True
    for val in data:
        if val == "(" or val == "[":
            stack.append(val)
        elif (val == ")" or val == "]") and stack:
            if stack[-1] == dic[val]:
                stack.pop()
            else:
                break
        elif val == ")" or val == "]"and len(stack) == 0:
            flag = False
            break

    if flag == False or stack:
        print("no")
    else:
        print("yes")