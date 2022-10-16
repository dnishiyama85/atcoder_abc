N = int(input())

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr


def factors(prime_factors):
    if len(prime_factors) == 0:
        return [1]

    ret = []
    p, a = prime_factors[-1]
    fs = factors(prime_factors[:-1])
    for b in range(2 * a + 1):
        fs1 = [(p**b) * f for f in fs]
        ret.extend([f for f in (p ** b) * fs1 if f <= N])

    return ret

result = set()

for k in range(1, N + 1):
    prime_factors = factorization(k)
    # fs = factors(prime_factors)
    # for i in fs:
    #     j = (k * k) // i
    #     if i <= N and j <= N:
    #         result.add((i, j))

print(len(result))
