import collections

n = int(input())
lst = list()
def group(wordList):
    group_dict = collections.defaultdict(list)
    for word in wordList:
        group_dict[len(word)].append(word)
    return group_dict

for case in range(n):
    word = input()
    if word in lst:
        continue
    else:
        lst.append(word)
result = group(lst)
idx = sorted(result.keys())
for i in idx:
    for word in sorted(result[i]):
        print(word)