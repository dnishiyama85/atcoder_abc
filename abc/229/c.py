n, w = list(map(int, input().strip().split()))
data = []
for _ in range(n):
    a, b = list(map(int, input().strip().split()))
    data.append((a, b))

# 貪欲法。
# おいしいチーズから載せられるだけ載せていく。

data = sorted(data, key=lambda d: d[0], reverse=True)
value = 0
weight = w
for a, b in data:
    if weight <= 0:
        break
    quant = min(b, weight)
    value += a * quant
    weight -= quant

print(value)
