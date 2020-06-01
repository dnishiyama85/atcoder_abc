n = int(input())

mbits = []

while abs(n) > 0:
    mbits.append(n % 2)
    n = n // 2 * (-1)

if len(mbits) == 0:
    mbits = [0]

ans = map(str, reversed(mbits))
ans = ''.join(ans)
print(ans)
