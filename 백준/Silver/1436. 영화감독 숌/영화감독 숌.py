import sys

input = sys.stdin.readline
n = int(input())
cnt = 0
num = 666
while True:
    if '666' in str(num):
        n = n-1
        if n == 0:
            break
    num += 1
    
print(num)