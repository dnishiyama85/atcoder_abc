N = int(input())
d = len(str(N))

# ちょうどd桁の整数を1つ書くとき、コンマは (d - 1) // 3 個書かれる。
# ちょうどd桁の整数を M 個書くとき、コンマは合計 M * (d - 1) // 3 個。
# 0以上 N 以下の整数を書くとき、 (= 1以上 N 以下の整数を書くとき)のコンマの合計は
# d = 1: 0 〜 9 → (9 - 0 + 1) * ((1 - 1) // 3)
# d = 2: 10 〜 99 → (99 - 10 + 1) * ((2 - 1) // 3)
# d = 3: 100 〜 999 → (999 - 100 + 1) * ((3 - 1) // 3)
# d = 4: 1000 〜 9999 → (9999 - 1000 * 1) * ((4 - 1) // 3)
# ...
# d = k: 10**(k - 1) 〜 10**k → (10**k - 10**(k-1)) * ((k - 1) // 3)

# したがって答えは、d - 1 桁までの分が
ans = 0
for k in range(1, d):
    ans += (10**k - 10**(k-1)) * ((k - 1) // 3)

# であり、残りが d 桁の部分で、
ans += (N - 10**(d-1) + 1) * ((d - 1) // 3)

# となる。
print(ans)
