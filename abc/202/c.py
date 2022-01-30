n = int(input())
as_ = list(map(int, input().strip().split()))
bs = list(map(int, input().strip().split()))
cs = list(map(int, input().strip().split()))

b_indices = [[] for _ in range(n + 1)]
for i, b in enumerate(bs):
    b_indices[b].append(i + 1)

c_counts = [0] * (n + 1)
for c in cs:
    c_counts[c] += 1

memo = [None] * (n + 1)
ans = 0
for i in range(n):
    a = as_[i]
    if memo[a] is not None:
        ans += memo[a]
    else:
        delta = 0
        indices = b_indices[a]
        for idx in indices:
            delta += c_counts[idx]
        memo[a] = delta
        ans += delta

print(ans)
