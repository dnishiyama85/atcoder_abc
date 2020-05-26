n, a, b = map(int, input().strip().split())

if (b - a) % 2 == 1:
    dt1 = a - 1
    dt1 += 1
    b1 = b - dt1
    t1 = dt1 + (b1 - 1) // 2

    dt2 = n - b
    dt2 += 1
    a1 = a + dt2
    t2 = dt2 + (n - a1) // 2
    print(min(t1, t2))
else:
    print((b - a) // 2)
