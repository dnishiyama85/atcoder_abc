import math

k = int(input())
gcd_bc = []
gcd_bb = []

for b in range(1, k + 1):
    gcd_bb.append(b)
    for c in range(b + 1, k + 1):
        gcd_bc.append(math.gcd(b, c))

total = 0
for a in range(1, k + 1):
    for d in gcd_bc:
        total += math.gcd(a, d) * 2

    for b in gcd_bb:
        total += math.gcd(a, b)

print(total)
