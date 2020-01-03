n, m = map(int, input().strip().split())
data = [list(map(int, input().strip().split())) for _ in range(n)]

data = sorted(data, key=lambda d: d[0])

shop = 0
cost = 0
bought = 0

while bought < m:
    price = data[shop][0]
    stock = data[shop][1]

    if m - bought <= stock:
        buy = m - bought
    else:
        buy = stock

    cost += price * buy
    bought += buy
    shop += 1

print(cost)
