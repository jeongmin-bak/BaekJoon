import math
import sys

input = sys.stdin.readline

def fun2(distance):
    max = int(math.sqrt(distance))
    if max == math.sqrt(distance):
        print(2 * max -1)
    elif distance <= (max * max + max):
        print(2 * max)
    else:
        print(2 * max+1)
    return


T = int(input())
for case in range(T):
    x, y = map(int, input().split())
    fun2(y-x)