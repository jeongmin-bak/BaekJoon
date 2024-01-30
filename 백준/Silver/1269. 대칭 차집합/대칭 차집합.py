import sys

input = sys.stdin.readline

An, Bn = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

sum = len(A.difference(B)) + len(B.difference(A))
print(sum)