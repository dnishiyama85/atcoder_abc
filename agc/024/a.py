a, b, c, k = map(int, input().strip().split())

for _ in range(k):
    a1 = b + c
    b1 = c + a
    c1 = a + b
    a, b, c = a1, b1, c1

ans = a - b
if abs(a - c) > 1e18:
    print('Unfair')
else:
    print(ans)
