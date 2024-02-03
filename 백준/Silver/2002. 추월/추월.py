
n = int(input())

in_dict = dict()
out_dict = dict()
for i in range(n):
    in_dict[input()] = i

for i in range(n):
    out_dict[input()] = i

cnt = 0
out_keys = list(out_dict.keys())
for i in range(len(out_dict)-1):
    now_in = in_dict[out_keys[i]]
    for j in range(i+1, len(out_keys)):
        next_in = in_dict[out_keys[j]]
        if next_in < now_in:
            cnt += 1
            break

print(cnt)