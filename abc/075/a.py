a, b, c = map(int, input().strip().split())

if a == b:
    print(c)
elif a == c:
    print(b)
elif b == c:
    print(a)

