n, a, b = map(int, input().strip().split())

if a > b:
    print(0)
elif n == 1 and a != b:
    print(0)
else:
    min_sum = a * (n - 1) + b
    max_sum = a + b * (n - 1)

    print(max_sum - min_sum + 1)
