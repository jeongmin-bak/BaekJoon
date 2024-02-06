import sys

input = sys.stdin.readline

n = int(input().rstrip())
for _ in range(n):
    password = input().rstrip()
    st = []
    st2 = []
    for c in password:
        if c == '<' and st:
            st2.append(st.pop())
        elif c == '>' and st2:
            st.append(st2.pop())
        elif c == '-' and st:
            st.pop()
        elif c != '<' and c != '>' and c != '-':
            st.append(c)

    st.extend(reversed(st2))
    print(''.join(st))