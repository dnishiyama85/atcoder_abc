from collections import defaultdict
n = int(input())

counts = defaultdict(int)
for _ in range(n):
    s = input().strip()
    if counts[s] == 0:
        print(s)
    else:
        print(f"{s}({counts[s]})")

    counts[s] += 1

