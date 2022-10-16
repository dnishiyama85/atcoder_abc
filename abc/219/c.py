x = list(input().strip())
n = int(input())
ss = []
for _ in range(n):
    s = input().strip()
    ss.append(s)

order_dict = {}
for i, a in enumerate(x):
    order_dict[a] = chr(ord('a') + i)

ss2 = []
for i, s in enumerate(ss):
    s2 = []
    for c in s:
        s2.append(order_dict[c])
    s2 = ''.join(s2)
    ss2.append((s2, i))

sorted_s2 = sorted(ss2, key=lambda s: s[0])

for s, i in sorted_s2:
    print(ss[i])





