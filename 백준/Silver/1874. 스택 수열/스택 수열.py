n = int(input())

stack, num, answer = [], 1, []
for case in range(0, n):
    data_input = int(input())
    while data_input >= num:
        stack.append(num)
        answer.append("+")
        num += 1
    if data_input == stack[-1]:
        stack.pop()
        answer.append("-")

if stack:
    print("NO")
else:
    for val in answer:
        print(val)