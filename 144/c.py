import math

n = int(input())
upper = int(math.sqrt(n))

mx = 1
for i in range(1, upper + 1):
    if n % i == 0:
        mx = i

h = mx
v = n // mx

move = h - 1 + v - 1

print(move)
