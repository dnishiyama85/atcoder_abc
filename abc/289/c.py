n, m = map(int, input().strip().split())
sets = []

for _ in range(m):
    _c = int(input())
    as_ = list(map(int, input().strip().split()))
    sets.append(as_)


def judge(ss):
    for j in range(1, n + 1):
        if all([j not in s for s in ss]):
            return False
    return True

count = 0
for b in range(2 ** m):
    selected = []
    for i in range(m):
        if b >> i & 1 == 1:
            selected.append(sets[i])

    if judge(selected):
        count += 1

print(count)
