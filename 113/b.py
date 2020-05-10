n = int(input())
t, a = map(int, input().strip().split())
hs = list(map(int, input().strip().split()))

best_i = 0
best_diff = 1e9

for i in range(n):
    h = hs[i]
    temp = t - 0.006 * h
    diff = abs(a - temp)
    if diff < best_diff:
        best_i = i
        best_diff = diff

print(best_i + 1)
