a, b, c, x, y = map(int, input().strip().split())

# AB ピザを何枚買うかを全探索
min_cost = 1e18
max_ab = 2 * max(x, y)
for i in range(max_ab + 1):
    cost = c * i
    rest_a = max(0, x - i // 2)
    rest_b = max(0, y - i // 2)
    cost += a * rest_a + b * rest_b
    min_cost = min(min_cost, cost)

print(min_cost)
