word = input()
croaia_a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croaia_a:
    word = word.replace(i, '*')
print(len(word))