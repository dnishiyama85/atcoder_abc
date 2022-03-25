T = int(input())

data = []
for _ in range(T):
    a, s = map(int, input().strip().split())
    data.append((a, s))

for a, s in data:
    ok = False
    d = s - 2 * a
    if d == 0:
        ok = True
    if d < 0:
        ok = False
    else:
        d %= a
        # a のゼロのビットの位置を調べる
        p = 0
        ps = []
        while a > 0:
            if a % 2 == 0:
                ps.append(p)
            a //= 2
            p += 1

        # d が 2**ps の組み合わせで表せればOK
        ps = sorted(ps, reverse=True)

        if d == 0:
            ok = True
        else:
            for p in ps:
                if d >= 2**p:
                    d -= 2**p
                if d == 0:
                    ok = True
                    break
    if ok:
        print('Yes')
    else:
        print('No')
