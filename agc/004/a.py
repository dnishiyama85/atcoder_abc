a, b, c = map(int, input().strip().split())

if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
    print(0)
else:
    ans = min([a * b, b * c, c * a])
    print(ans)
