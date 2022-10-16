n = int(input())
data = []
for _ in range(n):
    x, y = map(int, input().strip().split())
    data.append((x, y))

count = 0
for i in range(0, n - 2):
    for j in range(i, n - 1):
        for k in range(j, n):
            x1, y1 = data[i]
            x2, y2 = data[j]
            x3, y3 = data[k]

            if (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1):
                continue
            else:
                count += 1

print(count)
