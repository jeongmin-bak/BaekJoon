max_value = 0
for i in range(9):
    row = list(map(int, input().split()))
    new_max = max(row)

    if max_value <= new_max:
        max_value = new_max
        max_row = i+1
        max_col = row.index(new_max) + 1

print(max_value)
print(max_row, max_col)