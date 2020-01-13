from collections import defaultdict

n, k = map(int, input().strip().split())
as_ = map(int, input().strip().split())

dic = defaultdict(int)

for a in as_:
    dic[a] += 1

sorted_data = [(a, v) for a, v in dic.items()]
sorted_data = sorted(sorted_data, key=lambda d: d[1], reverse=True)

count = 0
while len(sorted_data) > k:
    count += sorted_data[-1][1]
    sorted_data.pop(-1)

print(count)
