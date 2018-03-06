import random

N = 100000
MAX = 1000000000

print(N)

for i in range(N):
    h = random.randint(1, MAX)
    s = random.randint(1, MAX)
    print("{} {}".format(h, s))
