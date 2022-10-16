x, a, d, n, = map(int, input().strip().split())

# 初項 a, 公差 d, 項数 n の等差数列 S の一般項は
# Sk = a + kd, k = 0, 1, ..., n - 1
if d < 0:
    a = a + (n - 1) * d
    d = -d

Sn = a + (n - 1) * d
min_s = min(a, Sn)
max_s = max(a, Sn)

if x <= min_s:
    ans = min_s - x
elif max_s <= x:
    ans = x - max_s
elif d == 0:
    ans = 0
else:
    # (x - a + ans) % d == 0 or (x - a - ans) % d == 0
    # ⇔ ans = d - (x - a) % d or ans = (x - a) % d
    ans = min(d - (x - a) % d, (x - a) % d)

print(ans)
