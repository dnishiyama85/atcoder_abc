n = int(input())
data = [list(map(int, input().strip().split())) for _ in range(n)]
data = sorted(data, key=lambda d: 2 * d[0] + d[1], reverse=True)

takahashi_ha = [d[1] for d in data]
aoki_ha = [d[0] for d in data]

takahashi_votes = 0
aoki_votes = sum(aoki_ha)

for i in range(n):
    takahashi_votes += takahashi_ha[i] + aoki_ha[i]
    aoki_votes -= aoki_ha[i]
    if takahashi_votes > aoki_votes:
        print(i + 1)
        exit(0)
