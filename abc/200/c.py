from scipy.special import comb

n = int(input())
as_ = list(map(int, input().strip().split()))

as_ = [a % 200 for a in as_]
counts = [0] * 200

for a in as_:
    counts[a] += 1

combinations = [0] * 200
for i, c in enumerate(counts):
    combinations[i] = comb(c, 2, exact=True)

ans = sum(combinations)
print(ans)
