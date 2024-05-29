from collections import Counter

sentence = list(input().lower().split())
print(sum(Counter(sentence).values()))