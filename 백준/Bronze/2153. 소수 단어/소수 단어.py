alpha_dict = dict()

for i in range(26):
    alpha_dict[chr(97+i)] = i+1
for i in range(26):
    alpha_dict[chr(65+i)] = i+26+1

def is_prime_num(n):
    for i in range(2,n):
        if n % i == 0:
            return "It is not a prime word."
    return "It is a prime word."
word = input()
sum = 0
for ch in word:
    sum += alpha_dict[ch]
print(is_prime_num(sum))