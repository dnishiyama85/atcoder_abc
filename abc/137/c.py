from collections import defaultdict

n = int(input())
strings = []
for i in range(n):
    s = sorted(input().strip())
    s = ''.join(s)
    strings.append(s)

counts = defaultdict(int)

for s in strings:
    counts[s] += 1

comb = 0
for v in counts.values():
    comb += v * (v - 1) // 2

print(comb)
