from collections import defaultdict

n, m = map(int, input().strip().split())
data = [list(map(int, input().strip().split())) for _ in range(m)]

prefectures = defaultdict(list)
for idx, (p, y) in enumerate(data):
    prefectures[p].append([idx, y, None])


for pref in prefectures:
    prefectures[pref].sort(key=lambda r: r[1])
    rows = prefectures[pref]
    for x, row in enumerate(rows):
        id = "{:06d}{:06d}".format(pref, x + 1)
        row[2] = id

all_list = []
for pref in prefectures.values():
    all_list.extend(pref)

all_list = sorted(all_list, key=lambda r: r[0])


for r in all_list:
    print(r[2])
