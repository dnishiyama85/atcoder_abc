n = int(input())
ps = list(map(int, input().strip().split()))

count = 0
for i in range(n):
    if ps[i] == i + 1:
        count += 1
        if i < n - 1:
            ps[i], ps[i + 1] = ps[i + 1], ps[i]
        else:
            ps[i], ps[i - 1] = ps[i - 1], ps[i]

print(count)
