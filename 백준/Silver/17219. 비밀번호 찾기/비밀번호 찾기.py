N, M = map(int, input().split())

myBook = dict()

for i in range(N):
    web, password = map(str, input().split())
    myBook[web] = password

for i in range(M):
    web = input()
    print(myBook.get(web))