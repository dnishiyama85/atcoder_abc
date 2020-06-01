a, b, x = map(int, input().strip().split())

left = 0
right = 1000000001


def digits(n):
    d = 0
    while n > 0:
        d += 1
        n //= 10

    return d


while right - left > 1:
    center = (left + right) // 2
    price = a * center + b * digits(center)
    if price <= x:
        left = center
    else:
        right = center

print(left)
