a, b, c = map(int, input().strip().split())

count = 0

while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    if a == b and b == c:
        count = -1
        break

    count += 1
    a1 = b // 2 + c // 2
    b1 = c // 2 + a // 2
    c1 = a // 2 + b // 2

    a, b, c = a1, b1, c1

print(count)
