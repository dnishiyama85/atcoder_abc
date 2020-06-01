n = int(input())
as_ = [int(input()) for _ in range(n)]

data = set()

for a in as_:
    if a not in data:
        data.add(a)
    else:
        data.remove(a)

print(len(data))
