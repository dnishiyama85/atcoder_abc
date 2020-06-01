n = int(input())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))

count = 0

for i in range(n):
    atk = b[i]
    if a[i] >= atk:
        kill = atk
        a[i] -= kill
    else:
        kill = a[i]
        atk -= a[i]
        a[i] = 0
        kill += min(a[i + 1], atk)
        a[i + 1] = max(a[i + 1] - atk, 0)

    count += kill

print(count)
