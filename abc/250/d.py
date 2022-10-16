import math

n = int(input())

# q^3 < n なる素数qをすべて列挙する。→ エラトステネスの篩

m = math.ceil(n ** (1/3))

primes = [True] * (m + 1)
primes[0] = False
primes[1] = False

i = 2
while i ** 3 <= n:
    for j in range(2 * i, m + 1, i):
        primes[j] = False

    i += 1

prime_nums = []

for i, flag in enumerate(primes):
    if flag:
        prime_nums.append(i)

count = 0
for q in prime_nums:
    for p in prime_nums:
        if p < q and p * q ** 3 <= n:
            count += 1
        else:
            break

print(count)
