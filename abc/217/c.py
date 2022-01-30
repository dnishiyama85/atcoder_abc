n = int(input())
ps = list(map(int, input().strip().split()))
qs = [0] * n

for i in range(n):
    qs[ps[i] - 1] = i + 1

print(" ".join(map(str, qs)))
