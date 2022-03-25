a, b, c, d = map(int, input().strip().split())

# 青木くんが勝つ = 任意の n (a <= n <= b) に対してある m (c <= m <= d) があり、
# n + m が素数になる。

# 素数判定
def is_prime(p):
    if p == 1:
        return False
    if p == 2:
        return True
    d = 2
    while True:
        if d * d > p:
            return True

        if p % d == 0:
            return False

        d += 1

aoki_win = True
# 全探索で行けそう？
for n in range(a, b + 1):
    found_for_n = False
    for m in range(c, d + 1):
        if is_prime(n + m):
            found_for_n = True
            break
    if not found_for_n:
        aoki_win = False

if aoki_win:
    print('Aoki')
else:
    print('Takahashi')
