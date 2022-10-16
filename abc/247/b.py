from collections import defaultdict

n = int(input())
data = []
for _ in range(n):
    s, t = input().strip().split()
    data.append((s, t))

possible = True
for i, (s, t) in enumerate(data):
    fs = True
    ft = True
    # s をあだ名とできるか
    for j, (s1, t1) in enumerate(data):
        if i != j:
            if s == s1 or s == t1:
                fs = False
            if t == t1 or t == s1:
                ft = False

    if (not fs) and (not ft):
        possible = False
        break

if possible:
    print('Yes')
else:
    print('No')
