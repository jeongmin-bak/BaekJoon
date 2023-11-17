N,K = list(map(int, input().split()))

lst = [x for x in range(1,N+1)]

idx = 0
delete = []
  
for num in range(N):
    idx += K-1
    if idx >= len(lst):
        idx = idx%len(lst)
    if len(lst) == 1:
        delete.append(lst[0])
    else:
        delete.append(lst[idx])
        lst.remove(lst[idx])
print("<"+ ", ".join(map(str, delete)) + ">")