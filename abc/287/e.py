n = int(input())
ss = []
keys = []
for i in range(n):
    s = input().strip()
    ss.append(s)
    keys.append(s)

ss = sorted(ss)

def calc_lcp(x, y):
    lcp = 0
    for cx, cy in zip(x, y):
        if cx == cy:
            lcp += 1
        else:
            break
    return lcp


lcps = {}
for i, s in enumerate(ss):
    if i == 0:
        lcps[s] = calc_lcp(s, ss[i+1])
    elif i == n - 1:
        lcps[s] = calc_lcp(s, ss[i-1])
    else:
        lcps[s] = max(calc_lcp(s, ss[i+1]), calc_lcp(s, ss[i-1]))


for s in keys:
    print(lcps[s])