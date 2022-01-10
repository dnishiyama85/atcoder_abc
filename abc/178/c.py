n = int(input())
nc2_2 = n * (n - 1)
powers = [1] * n
mod = 1000000007

total = 0
combs = [0] * (n + 1)
combs[1] = n
for i in range(2, n + 1):
    combs[i] = ((n + 1 - i) * combs[i - 1] // i) % mod

pow9i = 1
pow8i = 1

# 9 を何個含むかのループ
for i in reversed(range(1, n + 1)):
    # 9 を i 個含んで、残りの n - i 個は全く自由な組み合わせ（つまり 0〜8 の自由な組）の数
    pow9i = pow9i * 9 % mod
    pow8i = pow8i * 8 % mod
    comb = combs[i]
    free_i = (pow9i * comb) % mod
    # 9 を i 個含んで、残りの n - i 個に 0 を 1 個も含まない（つまり 1〜8 の自由な組）組み合わせ
    non_free_i = (pow8i * comb) % mod
    total = (total + (free_i - non_free_i)) % mod
    # print(i, total)

print(total)
