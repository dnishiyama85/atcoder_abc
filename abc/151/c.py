from collections import defaultdict

n, m = map(int, input().strip().split())
data = [input().strip().split() for _ in range(m)]

ac = defaultdict(int)
wa = defaultdict(int)

for p, s in data:
    if s == 'AC':
        ac[p] += 1
    else:
        if ac[p] == 0:
            wa[p] += 1

correct = 0
penalty = 0
for i in range(n + 1):
    p = str(i)
    if ac[p] > 0:
        correct += 1
        penalty += wa[p]

print(correct, penalty)
