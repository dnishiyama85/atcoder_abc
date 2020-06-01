a, b, k = map(int, input().strip().split())
result = set()

for small in range(a, min(a + k, b + 1)):
    result.add(small)

for large in range(max(a, b - k + 1), b + 1):
    result.add(large)

result = sorted(list(result))

for r in result:
    print(r)
