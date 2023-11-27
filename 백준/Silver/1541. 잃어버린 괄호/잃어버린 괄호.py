input_data = str(input())

str_data = input_data.split('-')
answer = 0
x = sum(map(int, (str_data[0].split('+'))))

if input_data[0] == '-':
    answer -= x
else:
    answer += x

for x in str_data[1:]:
    x = sum(map(int, (x.split('+'))))
    answer -= x
print(answer)