n = int(input())
data = [list(map(int, input().strip().split())) for _ in range(n)]

count = 0
for i in range(n):
    for j in range(i + 1, n):
        xi, yi = data[i]
        xj, yj = data[j]
        if xi == xj:
            continue
        grad = (yj - yi) / (xj - xi)
        if -1 <= grad and grad <= 1:
            count += 1

print(count)
