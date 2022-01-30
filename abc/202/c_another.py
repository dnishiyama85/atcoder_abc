n = int(input())
as_ = list(map(int, input().strip().split()))
bs = list(map(int, input().strip().split()))
cs = list(map(int, input().strip().split()))

# B_{Cj} = k となる個数を前もって数えておく。
b_counts = [0] * (n + 1)
for c in cs:
    k = bs[c - 1]
    b_counts[k] += 1

ans = 0
for a in as_:
    ans += b_counts[a]

print(ans)
