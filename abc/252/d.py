n = int(input())
as_ = list(map(int, input().strip().split()))

# i番目以降に a 以外の整数が何種類あるか
# i番目以降に a, b 以外の整数が何種類あるか

s = set()
as_rev = as_[::-1]

total = 0

for i, a in enumerate(as_rev):
    if i < 3:
        s.add(a)
    else:
        s.add(a)
        # print(s)
        l = len(s)
        if l >= 3:
            c = l * (l - 1) * (l - 2) // 3
            total += c

print(total)
