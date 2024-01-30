n = int(input())
book_list = list()
counter = {}
for case in range(n):
    book_name = input()
    book_list.append(book_name)
    if book_name not in counter:
        counter[book_name] = 0
    counter[book_name] += 1

books_key = sorted(counter)
max = -1
bestseller = ''
for key in books_key:
    if counter[key] > max:
        bestseller = key
        max = counter[key]
print(bestseller)