n = int(input())
ds = list(sorted(map(int, input().strip().split())))

k = 0
ans = 0

half = n // 2 - 1

if ds[half] == ds[half + 1]:
    print(0)
else:
    print(ds[half + 1] - ds[half])
