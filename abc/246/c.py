import heapq
n, k, x = map(int, input().strip().split())
items = list(map(int, input().strip().split()))

for i in range(n):
    items[i] *= -1

heapq.heapify(items)

# 各時点で一番高い商品にクーポンを使う。使ったら商品を値引きしてリストに入れなおす。
while k > 0 and len(items) > 0:
    a = -heapq.heappop(items)
    to_use = min(max(a // x, 1), k)
    new_price = a - to_use * x
    if new_price > 0:
        heapq.heappush(items, -new_price)

    k -= to_use

print(-sum(list(items)))
