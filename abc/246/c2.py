n, k, x = map(int, input().strip().split())
items = list(map(int, input().strip().split()))

for i in range(n):
    use = min(items[i] // x, k)
    items[i] -= use * x
    k -= use

if k > 0:
    items = sorted(items, reverse=True)
    for i in range(min(k, n)):
        items[i] = 0

print(sum(items))
