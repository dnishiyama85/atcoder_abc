from collections import defaultdict

n, k = map(int, input().strip().split())
as_ = list(map(int, input().strip().split()))

d = defaultdict(list)

for i, a in enumerate(as_):
    d[i % k].append(a)

sorted_d = {}

for i, array in d.items():
    sorted_d[i] = sorted(array)

# print(sorted_d)
final = []
for i in range(n // k + 1):
    for j in range(k):
        if j in sorted_d and i < len(sorted_d[j]):
            final.append(sorted_d[j][i])

# print(final)

if all(final[i] <= final[i+1] for i in range(len(final) - 1)):
    print('Yes')
else:
    print('No')

