from sys import stdin
import heapq
input = stdin.readline

n, q = map(int, input().strip().split())
data = [list(map(int, input().strip().split())) for _ in range(n)]
transfer = [list(map(int, input().strip().split())) for _ in range(q)]

kindergardens = [0] * 200000
for rate, kid in data:
    kindergardens[kid] = max(kindergardens[kid], rate)

equality = min(kindergardens)

# 転園
for c, d in transfer:
    # 幼児 c の所属が変わる
    # 幼稚園 d, e のレーティングが変わる
    rate_of_c = data[c - 1][0]
    e = data[c - 1][1]
    if kindergardens




