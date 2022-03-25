from collections import defaultdict

# n は高々 2^n <= 10^5 なる n しかない → 16くらい
n, x = map(int, input().strip().split())
data = []
for _ in range(n):
    line = list(map(int, input().strip().split()))
    as_ = line[1:]
    data.append(as_)

# i 番目の袋まで取り出したときにそれまでの数の総積が y になる組み合わせの数
# d[i, y] = sum_j d[i - 1, y // a_ij]

c0 = defaultdict(int)
for a0 in data[0]:
    c0[a0] += 1


def search(i, y):
    if i == 0:
        return c0[y]
    else:
        as_ = data[i]
        count = 0
        for a in as_:
            if y % a == 0:
                count += search(i - 1, y // a)
        return count


print(search(n-1, x))
