import random

n = 1000
s = ''
for i in range(n):
    c = random.choice(['R', 'G', 'B'])
    s += c

print(n)
print(s)


