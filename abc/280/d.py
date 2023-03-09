k = int(input())


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

    if arr == []:
        arr.append([n, 1])

    return arr

factors = factorization(k)

# N! に含まれる素因数 f の個数
def num_of_p_in_n_factorial(n, f):
    num = 0
    k = 1
    while n // f ** k > 0:
        num += n // f ** k
        k += 1

    return num


def check(n, factors):
    return all([num_of_p_in_n_factorial(n, f) >= p for f, p in factors])


left = 1
right = k
while left < right - 1:
    center = ((left + right) + 1) // 2
    if check(center, factors):
        right = center
    else:
        left = center

print(right)
