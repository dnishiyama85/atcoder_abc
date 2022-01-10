N = int(input())
A = map(int, input().strip().split())
counts = [0] * N
for a in A:
    counts[a - 1] += 1

for c in counts:
    print(c)
