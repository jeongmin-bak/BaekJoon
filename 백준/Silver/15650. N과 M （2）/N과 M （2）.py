import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
lst = [i for i in range(1,n+1)]
for ele in combinations(lst, m):
    print(str(list(ele)).replace("[", "").replace("]", "").replace(",", ""))