# 隣との距離が大きいところで担当区間を区切るのがお得。
# 各担当区間では行ったり来たりせずに端から端まで動くのがお得。

n, m = map(int, input().strip().split())
xs = sorted(list(map(int, input().strip().split())))
if n >= m:
    print(0)
elif n == 1:
    print(xs[-1] - xs[0])
else:
    intervals = sorted([(xs[i + 1] - xs[i], i) for i in range(m - 1)], reverse=True)

    divides = sorted([ind for _, ind in intervals[:n - 1]])

    total = 0
    for i in range(len(divides) + 1):
        if i == 0:
            interval = xs[divides[i]] - xs[0]
        elif i < len(divides):
            interval = xs[divides[i]] - xs[divides[i - 1] + 1]
        else:
            interval = xs[-1] - xs[divides[i - 1] + 1]

        total += interval

    print(total)
