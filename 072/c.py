n = int(input())
as_ = map(int, input().strip().split())

data = [0] * 100002

for a in as_:
    data[a] += 1

max_count = 0
for i in range(1, 100001):
    count = data[i - 1] + data[i] + data[i + 1]
    max_count = max(count, max_count)

print(max_count)
