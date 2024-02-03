import sys

input = sys.stdin.readline

n = int(input())
people = dict()
for case in range(n):
    person, commute = map(str, input().split())

    if person in people and commute == 'leave':
        people.pop(person)
    elif commute == 'enter':
        people[person] = commute

for person in sorted(people.keys(), reverse=True):
    print(person)