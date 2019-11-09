from operator import itemgetter

n = int(input())
data = []
for i in range(n):
    s, p = list(input().split())
    data.append((s, int(p), i + 1))

sorted_data = sorted(data, key=itemgetter(1), reverse=True)
sorted_data = sorted(sorted_data, key=itemgetter(0))

for s, p, i in sorted_data:
    print(i)

