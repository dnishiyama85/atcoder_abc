while True:
    n, x = map(int, input().strip().split())
    if n == 0 and x == 0:
        break

    ans = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                if i + j + k == x:
                    ans += 1

    print(ans)
