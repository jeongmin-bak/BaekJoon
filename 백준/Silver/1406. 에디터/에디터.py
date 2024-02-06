import sys
input = sys.stdin.readline
st1 = list(input().rstrip())
M = int(input())
st2 = list()
for _ in range(M):
    command = list(map(str, input().split()))
    if command[0] == 'P':
        st1.append(command[1])
    elif command[0] == 'L' and st1:
        st2.append(st1.pop())
    elif command[0] == 'D' and st2:
        st1.append(st2.pop())
    elif command[0] == 'B' and st1:
        st1.pop()

st1.extend(reversed(st2))
print(''.join(st1))